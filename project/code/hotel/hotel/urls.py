from django.contrib import admin
from django.urls import path
from hotelapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('customerlogin',views.customerlogin,name='customerlogin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('adminlink',views.adminlink,name='adminlink'),
    path('cusreg',views.cusreg,name='cusreg'),
    path('addroom',views.addroom,name='addroom'),
    path('room',views.room,name='room'),
    path('cuslog',views.cuslog,name='cuslog'),
    path('customerhome',views.customerhome,name='customerhome'),
    path('customerviewroom',views.customerviewroom,name='customerviewroom'),
    path('roomcheckin',views.roomcheckin,name='roomcheckin'),
    path('customercheckout',views.checkout,name='customercheckout'),
    path('checkout1',views.checkout1,name='checkout1'),
    path('adminviewcheckin',views.adminviewcheckin,name='adminviewcheckin'),
    path('adminviewcheckout',views.adminviewcheckout,name='adminviewcheckout'),
    path('adminviewcustomer',views.adminviewcustomer,name='adminviewcustomer'),

]
