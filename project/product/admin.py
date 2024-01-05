from django.contrib import admin
from .models import brandModel, productModel, UserCar ,comments
# Register your models here.

admin.site.register(brandModel)
admin.site.register(productModel)
admin.site.register(UserCar)
admin.site.register(comments)