from django.contrib import admin
from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.home, name= "index"),
    path('competitions', views.competitions, name= "competitions"),
    path('competition-edit', views.competition_edit, name= "competition-edit"),
    path('account', views.account, name= "account"),
    path('account-edit', views.account_edit, name= "account-edit"),
    path('koi', views.koi, name= "koi"),
    path('koi-edit', views.koi_edit, name= "koi-edit"),
    
]

