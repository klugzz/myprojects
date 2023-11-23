from django import forms
from webapps.models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'
