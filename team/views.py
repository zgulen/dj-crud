from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from team.models import Student
from .forms import StudentForm
from django.contrib import messages


def student_page(request):
    form = StudentForm()
    print(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Student Added Succesfully')
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'team/student_form.html', context)

def student_update(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            messages.success(request, 'Student updated Succesfully')
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'team/student_update.html', context)

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    print(students)
    return render(request, 'team/home.html', context)

def student_delete(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    context={
        'student':student
    }
    return render(request, 'team/student_delete.html', context)