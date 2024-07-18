from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('set-open-time/', set_open_time, name='set_open_time'),
    path('', list, name = 'main'),
    path('modify-open-time/', modify_time, name='modify_open_time'),
    path('update/<int:id>/', update, name="update"),
]