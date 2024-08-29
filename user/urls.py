from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('', user, name= 'list'),
    path('add/', add, name= 'add_user'),
    path('update/<str:pk>', edit, name= 'edit_user'),
    path('delete/<str:pk>', delete, name='delete'),
]