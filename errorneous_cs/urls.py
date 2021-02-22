from django.urls import path
from . import views
app_name = 'errorneous_cs'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutpage, name="logout")
]
