from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'genre': forms.RadioSelect,
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }