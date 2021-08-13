#specific urls.py for app1

from django.urls import path,include
from app1.views import *
app_name='app1'
urlpatterns = [
    path('app1/',app1_function,name='app1'),
    
]