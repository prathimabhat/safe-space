from django import forms
from django.forms import ModelForm
from .models import question_to_therapist
from ckeditor.widgets import CKEditorWidget
class QuestionForm(forms.ModelForm):
    
	question=forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control','placeholder': 'Type here'}))

	class Meta:
		model=question_to_therapist
		fields=['question']
		'''widgets={

	    		'question':forms.Textarea(attrs={'class':'form-control','label':'question','placeholder': 'Type here...'})
	    	}'''

   
