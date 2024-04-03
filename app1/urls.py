from django.urls import path
from app1.views import *
app_name='samsung'

urlpatterns=[
    path('fun1/',fun1,name='fun1'),
    path('fun/',fun,name='fun'),
]