from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import RegisterUserForm, LogInUserForm
# Create your views here.

def RegisterUser(request):

	#Register
	GetRegisterUserForm = RegisterUserForm(request.POST or None)
	if GetRegisterUserForm.is_valid():
		user = GetRegisterUserForm.save()
		password = GetRegisterUserForm.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		
	#Log-In
	LogInUser = LogInUserForm(request.POST or None)
	if LogInUser.is_valid():
		username = LogInUser.cleaned_data.get("username")
		password = LogInUser.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)

	context = {
		"RegisterUserForm":GetRegisterUserForm,
		'LogInUser':LogInUser
	}
	
	return render(request,"login.html",context)
