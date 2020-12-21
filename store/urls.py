from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('signout/', views.signoutView, name='signout'),

]
