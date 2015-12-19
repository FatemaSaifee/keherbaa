from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone
from django.contrib import auth

from .models import Product, ProductType, ProductTypeBlock
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import pdb

# Create your views here.
class IndexView(ListView):
    model = Product
    template_name = 'paints/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['product_list'] = Product.objects.all()
        
        
        return ctx

class AboutusView(ListView):
    model = Product
    template_name = 'paints/aboutus.html'

    def get_context_data(self, **kwargs):
        ctx = super(AboutusView, self).get_context_data(**kwargs)
        ctx['product_list'] = Product.objects.all()
        
        
        return ctx