from django.urls import path
from .views import student_page, student_list,student_update,student_delete

urlpatterns = [
    path('', student_list, name='home'),
    path('student/', student_page, name='student'),
    path('update/<int:id>', student_update, name='update'),
    path('delete/<int:id>', student_delete, name='delete'),
]