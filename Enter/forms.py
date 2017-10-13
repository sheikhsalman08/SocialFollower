from django import forms
from django.contrib.auth import (
								authenticate,
								get_user_model,
								login,
								logout,
								)
from django.contrib.auth.models import User

User = get_user_model()

class RegisterUserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input','id':'pass'}))
	email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'autocomplete':'off','class':'input','id':'pass'}))
	email2 = forms.EmailField(label='Repeat Email',widget=forms.TextInput(attrs={'autocomplete':'off','class':'input','id':'pass'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':'off','class':'input','id':'pass'}))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':'off','class':'input','id':'pass'}))

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
			'password2',
		]
	def clean(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Email must match")

		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError("Password didn't match")

		username = self.cleaned_data.get('username')
		username_qs = User.objects.filter(username = username)

		email_qs = User.objects.filter(email = email)
		if email_qs.exists():
			raise forms.ValidationError("This email hsa already been registered")
		
		return super(RegisterUserForm,self).clean(*args,**kwargs)	

class LogInUserForm(forms.Form):
	# username = forms.CharField()


	username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input','id':'pass','data-type':'password'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'input','data-type':'password'}))



	def clean(self,*args,**kwargs):


		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("Try Again")
			if not user.check_password(password)			:
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is no longer active")
		return super(LogInUserForm, self).clean(*args,**kwargs)
