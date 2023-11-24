from django import forms
from Bankapps.models import Bank

class BankForm(forms.ModelForm):
	class Meta:
		model=Bank
		fields='__all__'