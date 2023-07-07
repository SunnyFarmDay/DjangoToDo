from django.urls import path, include
from . import views

# declare the url and connects to the view functions in views.py
urlpatterns = [
    path('', views.hello_world)
]
