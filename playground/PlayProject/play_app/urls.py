from django.urls import path
from play_app import views

urlpatterns = [
    path('', views.user, name='users'),
]