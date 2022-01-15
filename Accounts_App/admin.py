from django.contrib import admin

# Register  models here.
from .models import User
from .models import Product

admin.site.register(User)
admin.site.register(Product)