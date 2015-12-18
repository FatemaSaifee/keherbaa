from django.contrib import admin
from paints.models import Product, ProductType, ProductTypeBlock
# Register your models here.

class ProductTypeInline(admin.StackedInline):
	model = ProductType
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductTypeInline]

admin.site.register(Product, ProductAdmin)