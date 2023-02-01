from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', auto.as_view(), name='auto'),
    path('car/<slug:car_slug>/', car_show.as_view(), name='car'),
    path('brand/<slug:brand_slug>/', cache_page(60)(car_brand.as_view()), name='brand'),
]

# path('post/<slug:post_slug>/', post_show.as_view(), name='post'),
