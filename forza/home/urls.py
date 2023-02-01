from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LoggoutUser.as_view(), name='logout'),
    path('contact/', Contact.as_view(), name='contact'),
]