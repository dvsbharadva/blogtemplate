from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name="home" ),
    path('<slug:slug>/', views.postDetail , name="post_detail")
]