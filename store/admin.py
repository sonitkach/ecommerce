from django.contrib import admin
from .models import Customer, Order, OrderedItem, Address, Product

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(Address)
admin.site.register(Product)
