from django import forms
from . import models

class CriarNome(forms.ModelForm):
	class Meta:
		model = models.Nome 
		fields = ['nome', 'significado', 'slug']
		