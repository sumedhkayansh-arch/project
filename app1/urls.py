from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path("menu",views.menu),
    path("north_indian",views.north_indian),
    path("south_indian",views.south_indian),
    path("starters",views.starters),
    path("chinese",views.chinese),
    path("pizzas_burgers",views.pizzas_burgers),
    path("dessert",views.dessert),
    path("contact_us",views.contact_us),
    path("about_us",views.about_us),
    path("profile",views.profile),
    path("log_in",views.log_in),
    path("sign_in",views.sign_in)
]