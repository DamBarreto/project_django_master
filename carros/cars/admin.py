from django.contrib import admin

# APP IMPORTS
from .models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand__name')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)