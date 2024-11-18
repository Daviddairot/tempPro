from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('upload-numbers/', views.updateTemperature, name='upload_numbers'),
]