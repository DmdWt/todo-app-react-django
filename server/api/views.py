from django.shortcuts import render
from django.urls import path
from .views import HelloWorld

urlpatterns = [
    path("hello/", HelloWorld.as_view()),
]

# Create your views here.
