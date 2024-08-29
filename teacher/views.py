from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

# Create your views here.

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher/list.html", {'teachers': teachers})

def add(request):
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('teacher:list')
    else:
        teacher_form = TeacherForm()
    return render(request, "teacher/add.html", {'teacher_form':teacher_form})

def edit(request, pk):
    if request.method == "POST":
        teacher = Teacher.objects.get(id=pk)
        teacher_form =TeacherForm(request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('teacher:list')
    else:
        teacher = Teacher.objects.get(id=pk)
        teachers = TeacherForm(instance=teacher)
        
        return render(request, "teacher/edit.html", {'teachers':teachers})
    
def delete(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    
    return redirect('teacher:list')