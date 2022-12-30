from django.urls import path
from app1.views import *
app_name='some2'
urlpatterns=[
    path('second/',second,name='second'),
]