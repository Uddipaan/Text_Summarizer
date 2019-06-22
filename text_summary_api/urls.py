from django.urls import path
from . import views

urlpatterns = [
    path('summary', views.summary)
]
