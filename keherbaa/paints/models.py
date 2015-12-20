from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)

	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class ProductType(models.Model):
	product = models.ForeignKey(Product)
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)

	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class ProductTypeBlock(models.Model):
	productType = models.ForeignKey(ProductType)
	name= models.CharField(max_length=100)

	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class ProductTypeBlockPoint(models.Model):
	productTypeBlock = models.ForeignKey(ProductTypeBlock)
	point= models.CharField(max_length=100)

	def __unicode__(self):  # Python 3: def __str__(self)
		return self.point