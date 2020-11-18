from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
	username=forms.CharField(label='Enter a username',widget=forms.TextInput(attrs={'placeholder':'NinjaGirl','size':'40'}))
	email=forms.EmailField(label='Enter your email address',widget=forms.EmailInput(attrs={'placeholder': 'jondoe@example.com','size':'40'}))
	first_name=forms.CharField(label='Enter your first name',widget=forms.TextInput(attrs={'placeholder':'Jon','size':'40'}))
	last_name=forms.CharField(label='Enter your last name',widget=forms.TextInput(attrs={'placeholder':'Doe','size':'40'}))

	date_of_birth = forms.DateField(label='Enter your date of birth',widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD','size':'40','class':'datetime-input'}))
	location=forms.CharField(label='Where are you from?',widget=forms.TextInput(attrs={'placeholder': 'eg. Bangalore,India','size':'40'}))
	reason=forms.CharField(label='Why do you want to join our community?',widget=forms.Textarea(attrs={'placeholder': 'I want to join because...','size':'45'}))
	
	password1=forms.CharField(label='Enter a password',widget=forms.PasswordInput(attrs={'size':'40'}))
	password2=forms.CharField(label='Enter your password again',widget=forms.PasswordInput(attrs={'size':'40'}))
	class Meta:
		model = CustomUser
	
		fields = ['username', 'email', 'first_name', 'last_name',  'date_of_birth', 'location', 'reason','password1', 'password2']

	