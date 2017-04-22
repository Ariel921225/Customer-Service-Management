from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Service_Request)
admin.site.register(Shipping_Address)
admin.site.register(Billing_Address)
admin.site.register(Payment_Method)
admin.site.register(Security)