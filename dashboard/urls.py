from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dasboard/', views.dashboardAction),
]