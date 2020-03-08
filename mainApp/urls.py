from django.urls import path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
