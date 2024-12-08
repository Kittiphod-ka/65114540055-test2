from django.urls import path
from .views import *
urlpatterns = [
    path('course/',course_list ,name='course_list'),
]