from django.urls import path
from app2.views import *
app_name='realme'

urlpatterns=[
    path('fun2/',fun2,name='fun2'),
]