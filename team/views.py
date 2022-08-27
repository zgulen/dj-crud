from django.shortcuts import render
from django.views.generic import TemplateView
from team.models import Student
from .forms import StudentForm
from django.contrib import messages



def student_page(request):
    form = StudentForm()
    query = request.POST
    print(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Student Added Succesfully')
    context = {
        'form':form,
        'query': query
    }
    return render(request, 'team/student_form.html', context)

def student_update(request):
    pass