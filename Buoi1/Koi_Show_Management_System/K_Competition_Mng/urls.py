from django.urls import path
from . import views

urlpatterns = [
    path('K_Competition_Mng/', views.competition, name='K_Competition_Mng'),
]