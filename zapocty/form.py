from django import forms
from zapocty.models import Student,Predmet,Zapocet

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
class PredmetForm(forms.ModelForm):
	class Meta:
		model = Predmet
class ZapocetForm(forms.ModelForm):
	class Meta:
		model = Zapocet
