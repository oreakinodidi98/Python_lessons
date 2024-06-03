from django.urls import path
from .views import view_home, view_welcome, sports

urlpatterns = [
    path("", view_home, name="home"),
    path("welcome/", view_welcome, name="welcome"),
    path("sports/", sports, name="sports")
]