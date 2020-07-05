from django.shortcuts import render,redirect
import datetime
from django.core.mail import send_mail
from datetime import datetime,date
import csv
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import Group
from.models import *
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm,ProductForm,CustomerForm,Createuser,Monthbills,Contactform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from.deco import unauth_user,allowed_users,admin_only
from.filters import Productfilter,Orderfilter
from django.views.generic import View
# Create your views here

@unauth_user
def registrationform(request):
        form=Createuser()
        if request.method=='POST':
            form=Createuser(request.POST)
            if form .is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                group=Group.objects.get(name='customers')
                user.groups.add(group)
                messages.success(request,'Account was created '+username)
                return redirect('loginform')
        context={'form':form}
        return render(request,'main/registrationform.html',context)
@unauth_user
def loginform(request):

        if request.method=='POST':
           username= request.POST.get('username')
           password= request.POST.get('password')
           user=authenticate(request,username=username,password=password)
           if user is not None:
                login(request,user)
                return redirect('/')
           else:
               messages.info(request,'Username or Password was incorrect')
        context={}
        return render(request,'main/login.html',context)
def logoutuser(request):
    logout(request)
    return redirect('loginform')
def userpage(request):
    customer = Customer.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    total_customers = customer.count()
    context = {'customer': customer, 'orders': orders, 'total_customers': total_customers, 'products': products}
    return render(request, 'main/user.html', context)


@login_required(login_url='loginform')
@admin_only
def home(request):
    customer = Customer.objects.all()
    orders = Order.objects.all()
    products=Product.objects.all()
    total_customers = customer.count()
    context = {'customer': customer, 'orders': orders, 'total_customers': total_customers,'products':products}
    return render(request, 'main/dashboard.html', context)

@login_required(login_url='loginform')
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    order=customer.order_set.all()
    product=customer.product_set.all()
    order1=Orderfilter(request.GET,queryset=order)
    myfilter=Productfilter(request.GET,queryset=product)
    context = {'customer':customer,'product':product,'myfilter':myfilter,'order1':order1,'order':order}
    product=myfilter.qs
    order=order1.qs
    return render(request,'main/customerbills.html',context)



@login_required(login_url='loginform')
def products(request):
    now=date.today()
    products=Product.objects.all()




    go =products
    global total_prices
    global f
    total_prices = sum(product.price for product in products)
    f=int(total_prices)
    context={'products':products,'f':f,'go':go}
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == 'customers':
     if now.day==4:

         products.delete()
         f=0
         return render(request, 'main/products1.html', context)

     else:
         return render(request, 'main/products2.html', context)

    if group == 'admin':
        print()
    if now.day==4:
        products.delete()
        return render(request, 'main/products1.html', context)

    else:
        return render(request, 'main/products.html', context)

@login_required(login_url='loginform')
def createcustomer(request):
    form=OrderForm

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'main/createcustomer.html',context)
def deletecustomer(request,pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context={'customer':customer,}
    return render(request,'main/deletecustomer.html',context)
@login_required(login_url='loginform')
def Member(request):
    form=CustomerForm

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'main/createcustomer.html',context)

@login_required(login_url='loginform')
def createproduct(request):
    form=ProductForm

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'main/createcustomer.html',context)

@login_required(login_url='loginform')
def updateorder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request,'main/createcustomer.html',context)
def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request,'main/delete.html',context)
def updateproduct(request,pk):
    product=Product.objects.get(id=pk)
    form=ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'main/createcustomer.html', context)

def deleteproduct(request,pk):
    product =Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    context={'item':product}
    return render(request,'main/delete1.html',context)

def monthbills(request):
    products(request)
    flag=Bills.objects.all().count()
    bills=Bills.objects.all()
    go=bills

    print(flag)
    total_prices1 = sum(bill.price for bill in bills)
    eo=int(total_prices1)
    sub=f-eo

    context={'bills':bills,'sub':sub,'flag':flag,'go':go}
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        now = date.today()
    if group == 'customers':

        if  now.day == 3:
            bills.delete()
            sub=0
            return render(request, 'main/monthbills1.html', context)
        else:
            return render(request, 'main/monthbills.html', context)





    if group == 'admin':
        return render(request, 'main/monthbills.html', context)


def createmonthbills(request):
    form=Monthbills
    now = date.today()

    if request.method == 'POST':
        form = Monthbills(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'main/createbills.html',context)
def deletebill(request,pk):
    bill =Bills.objects.get(id=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('/')

    context={'item':bill}
    return render(request,'main/deletebill.html',context)

def updatebill(request,pk):
     bill=Bills.objects.get(id=pk)
     form=Monthbills(instance=bill)
     if request.method == 'POST':
        form = Monthbills(request.POST,instance=bill)
        if form.is_valid():
            form.save()
            return redirect('/')
     context = {'form': form}

     return render(request, 'main/createbills.html', context)

def export(request):
    response=HttpResponse(content_type='text/csv')

    writer =csv.writer(response)
    writer.writerow(['Customer','bills','price'])
    def __str__(self):
        return str(self.customer)

    for bills in Bills.objects.all().values_list('Customer', 'bills', 'price'):
        writer.writerow(bills)

    response['Content-Disposition'] = 'attachment; filename="month.csv"'

    return response

def resultdata(request):
    billsdata=[]

    door=Bills.objects.all()
    for i in door:
        billsdata.append({i.bills:i.price})
    return JsonResponse(billsdata,safe=False)

def contactus(request):
    form=Contactform
    if request.method=='POST':
        form=Contactform(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            messages = "{0} has sent you a new message :\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', messages, sender_email, ['sathwikthop@gmail.com'])
            return redirect('/')

    else:
        return render(request,'main/contactform.html',{'form': form})
def billschart(request):
    return render(request,'main/barchat.html')