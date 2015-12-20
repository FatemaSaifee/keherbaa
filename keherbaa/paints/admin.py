from django.contrib import admin
from nested_admin import NestedAdmin, NestedStackedInline
from paints.models import Product, ProductType, ProductTypeBlock, ProductTypeBlockPoint
# Register your models here.

class ProductTypeBlockPointInlines(NestedStackedInline):
	model = ProductTypeBlockPoint
	extra =2

class ProductTypeBlockInline(NestedStackedInline):
	model = ProductTypeBlock
	inlines = [ProductTypeBlockPointInlines,]

class ProductTypeInline(NestedStackedInline):
	model = ProductType
	extra = 1
	inlines = [ProductTypeBlockInline,]

class ProductAdmin(NestedAdmin):
	inlines = [ProductTypeInline,]

admin.site.register(Product, ProductAdmin)
