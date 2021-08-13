#specific urls.py for app1

from django.urls import path,include

from app2.views import *
app_name='app2'
urlpatterns = [
    path('app2/',app2_function,name='app2'),
    
]