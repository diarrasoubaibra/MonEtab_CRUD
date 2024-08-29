from django.urls import path
from .views import *


app_name = 'student'
urlpatterns = [
    path('', student, name= 'list'),
    path('add/', add, name= 'add_student'),
    path('update/<str:pk>', edit, name= 'edit_student'),
    path('delete/<str:pk>', delete, name='delete'),
]