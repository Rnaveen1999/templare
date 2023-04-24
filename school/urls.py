from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Homepage , name = 'Homepage'),
    path('table/',views.Table , name = 'table'),
]