from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email