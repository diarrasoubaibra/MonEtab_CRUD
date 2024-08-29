from django.urls import path
from .views import *

app_name = 'teacher'
urlpatterns = [
    path('', teacher, name= 'list'),
    path('add/', add, name= 'add_teacher'),
    path('update/<str:pk>', edit, name= 'edit_teacher'),
    path('delete/<str:pk>', delete, name='delete'),
]