from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('chipotle', views.message_redirect, name='message_redirect'),
    path('chipotle', views.send_sms, name='send_sms'),
]
