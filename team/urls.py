from django.urls import path
from .views import student_page, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('student/', student_page, name='student')
]