from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('set-open-time/', set_open_time, name='set_open_time'),
    path('', main, name = 'main'),
    path('modify-open-time/', modify_time, name='modify_open_time'),
    path('message_list/', message_list, name = 'message_list'),
    path('message_create/', message_create, name = 'message_create'),
]