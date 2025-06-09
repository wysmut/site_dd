from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('testing/', views.testing, name='testing'),
path('dashboard/', views.dashboard, name='dashboard'),
path('login/', views.login_view, name='login'),
]
