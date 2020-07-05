from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from. import views
urlpatterns = [
    path('registration/', views.registrationform,name="registrationform"),

    path('login/', views.loginform, name="loginform"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('user/', views.userpage, name="userpage"),
    path('', views.home,name="home"),
    path('products/', views.products,name="products"),
    path('customer/<str:pk>/', views.customer,name="customer"),
    path('Member/', views.Member,name="Member"),
    path('createcustomer/',views.createcustomer,name="createcustomer"),
    path('deletecustomer/<str:pk>/', views.deletecustomer, name="deletecustomer"),
    path('createproduct/',views.createproduct,name="createproduct"),
    path('updateorder/<str:pk>/',views.updateorder,name="updateorder"),
    path('deleteorder/<str:pk>/',views.deleteorder,name="deleteorder"),
    path('updateproduct/<str:pk>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<str:pk>/', views.deleteproduct, name="deleteproduct"),
    path('deleteproduct/<str:pk>/', views.deleteproduct, name="deleteproduct"),
    path('monthbills/', views.monthbills,name="monthbills"),
    path('createmonthbills/', views.createmonthbills,name="createmonthbills"),
    path('updatebill/<str:pk>', views.updatebill, name="updatebill"),
    path('deletebill/<str:pk>', views.deletebill, name="deletebill"),
    path('export/', views.export, name="export"),
    path('resultdata/',views.resultdata,name="resultdata"),
    path('contact/', views.contactus, name="contactus"),
    path('billschart/', views.billschart, name="billschart"),



    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="main/passwordreset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="main/passwordresetsent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="main/passwordresetform.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="main/passwordresetdone.html"),
         name="password_reset_complete"),
    ]


