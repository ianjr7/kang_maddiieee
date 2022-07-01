from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_home, name="login_home"),
    path('homee/', views.home, name="homee"),
    path('logout/', views.logout_user, name="logout"),
    path('okk/', views.later, name="later"),
    path('accounts/google/login/callback/home/', views.index, name="home"),
    path('meetings/', views.meetings, name="meetings"),



    path('about', views.about, name="about"),
]
