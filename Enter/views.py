from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.views.generic import DetailView
from .forms import RegisterUserForm, LogInUserForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def EnterUser(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')

	#Log-In
	if request.method == 'POST' and 'sign_in' in request.POST:
		LogInUser = LogInUserForm(request.POST or None)
		GetRegisterUserForm = RegisterUserForm
		if LogInUser.is_valid():
			username = LogInUser.cleaned_data.get("username")
			password = LogInUser.cleaned_data.get("password")
			user = authenticate(username = username, password = password)
			login(request, user)
			return HttpResponseRedirect('/')

	#Register
	elif request.method == 'POST' and 'sign_up' in request.POST:
		LogInUser = LogInUserForm
		GetRegisterUserForm = RegisterUserForm(request.POST or None)
		if GetRegisterUserForm.is_valid():
			user = GetRegisterUserForm.save()
			password = GetRegisterUserForm.cleaned_data.get('password')
			user.set_password(password)
			user.save()

			new_user = authenticate(username = user.username, password = password)
			login(request, new_user)
			return HttpResponseRedirect('/')

	else:
		LogInUser = LogInUserForm
		GetRegisterUserForm = RegisterUserForm

	context = {
		'LogInUser':LogInUser, 
		"RegisterUserForm":GetRegisterUserForm
	}
	
	return render(request,"login.html",context)
