from django.urls import path
from app2.views import *
app_name='something1'

urlpatterns=[
    path('latha/',latha,name='latha'),
    path('joshi/',joshi,name='joshi'),
]