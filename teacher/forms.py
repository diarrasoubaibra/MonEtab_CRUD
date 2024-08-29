from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect,
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }