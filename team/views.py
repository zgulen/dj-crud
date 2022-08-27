from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from team.models import Student
from .forms import StudentForm
from django.contrib import messages


def home_page(request):
    return render(request, 'team/base.html')


def student_page(request):
    form = StudentForm()
    print(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Student Added Succesfully')
            return redirect('')
    context = {
        'form':form
    }
    return render(request, 'team/student_form.html', context)

def student_update(request):
    pass