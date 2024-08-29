from django.urls import path
from .views import *

app_name = 'report'
urlpatterns = [
    path('', report, name= 'report'),
]