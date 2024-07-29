from django.urls import path
from . import views

urlpatterns = [
        path('', views.logindex, name="logindex")
        ]
