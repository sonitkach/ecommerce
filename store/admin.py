from django.contrib import admin
from .models import Customer, Order, OrderItem, Address, Product

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Product)
