from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(post_list.as_view()), name='news'),
    path('post/<slug:post_slug>/', post_show.as_view(), name='post'),
    path('category/<slug:cat_slug>/', cache_page(60)(post_category.as_view()), name='category'),
    path('add_post/', post_add.as_view(), name='add_post'),
    path('category/<slug:cat_slug>/add_post/', post_add.as_view(), name='add_post'),
]