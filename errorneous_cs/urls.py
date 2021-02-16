from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.SignView, name="register"),
    path('login/', views.LoginView, name="login"),
]
