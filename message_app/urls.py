from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chipotle', views.message_redirect, name='message_redirect'),
]
