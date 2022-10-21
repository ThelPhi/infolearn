from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('topic/<str:pk>/', views.topic, name="topic"),
    path('category/<str:cat>/', views.category, name="category"),

    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutPage, name="logout")
]