from django.contrib import admin
from django.conf.urls import url, include
from api import views

urlpatterns = [
    url('^location/', views.ApiView.as_view(), name="api-location"),
]