from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.resetPassword),
    path('reset-password/', views.resetPasswordAction),
]