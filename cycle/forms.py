from django.forms import ModelForm
from django.contrib.auth .forms import UserCreationForm
from django.contrib.auth.models import User
from.models import *
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields=['customer','works','status']


class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields=['customer','category','price']

class CustomerForm(ModelForm):
    class Meta:
        model= Customer
        fields = '__all__'

class Createuser(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','email','password1','password2']
class Monthbills(ModelForm):
    class Meta:
        model=Bills
        fields='__all__'

class Contactform(forms.Form):
    name=forms.CharField(max_length=200)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)

