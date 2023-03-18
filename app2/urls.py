from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('jadeja/',jadeja,name='jadeja'),
    path('rohit/',rohit,name='rohit'),
]