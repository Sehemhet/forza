from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Brands, Cars, TypeDrive

class auto(ListView):
    paginate_by = 12
    model = Brands
    template_name = 'auto/auto.html'
    context_object_name = 'auto'


    def get_queryset(self):
        return Brands.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class car_brand(ListView):
    paginate_by = 6
    model = Cars
    template_name = 'auto/model.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Cars.objects.filter(brand__slug=self.kwargs['brand_slug'])

class car_show(DetailView):
    model = Cars
    context_object_name = 'car'
    template_name = 'auto/car.html'
    slug_url_kwarg = 'car_slug'




