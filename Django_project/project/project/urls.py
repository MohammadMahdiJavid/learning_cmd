"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('lesson1/', views.exercise_number_1),
    path('lesson2/', views.exercise_number_2),
    path('lesson3/', views.exercise_number_3),
    path('lesson4/', views.exercise_number_4),
    path('lesson5/', views.exercise_number_5),
    path('lesson6/', views.exercise_number_6),
    path('lesson7/', views.exercise_number_7),
    path('lesson8/', views.exercise_number_8),
    path('lesson9/', views.exercise_number_9),
    path('lesson10/', views.exercise_number_10),
    path('lesson11/', views.exercise_number_11),
    path('lesson12/', views.exercise_number_12),
    path('lesson13/', views.exercise_number_13),
    path('lesson14/', views.exercise_number_14),
    path('lesson15/', views.exercise_number_15),
    path('lesson16/', views.exercise_number_16),
    path('mainpage/', views.main_page),
    #path('namesearch/', views.nameresult),
    path('lesson1/check_command/', views.check_command),





]