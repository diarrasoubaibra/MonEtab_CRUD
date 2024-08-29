from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.

def student(request):
    students = Student.objects.all()
    return render(request, "student/list.html", {'students': students})

def add(request):
    if request.method == "POST":
        stud_form = StudentForm(request.POST)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('student:list')
    else:
        stud_form = StudentForm()
    return render(request, "student/add.html", {'stud_form':stud_form})


def edit(request, pk):
    if request.method == "POST":
        student = Student.objects.get(id=pk)
        stud_form =StudentForm(request.POST, instance=student)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('student:list')
    else:
        student = Student.objects.get(id=pk)
        students = StudentForm(instance=student)
        
        return render(request, "student/edit.html", {'students':students})
    
def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student:list')