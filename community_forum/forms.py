from django import forms
from django.forms import ModelForm
from .models import Answers
from ckeditor.widgets import CKEditorWidget
class AnswerForm(forms.ModelForm):

   
	answer=forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control','placeholder': 'Type here'}))

	class Meta:
		model=Answers
		fields=['answer']
		
   
