from django.shortcuts import render,redirect
from django.utils.timezone import now

from .models import Order
from .forms import FreeOrderForm, PremiumOrderForm
from django.views.generic import View

from django.contrib import messages 
# Create your views here.


class FreeOrder(View):
<<<<<<< HEAD

	def get(self,request):
		
=======
	
	def get(self,request):
>>>>>>> b775cee5636e160ad176f7e505afa8b1133d6724
		orderForm = FreeOrderForm()
		context = {
			'FreeOrderForm': orderForm,
			'CurrentUser':request.user.id,
			'CurrentTime':now(),
		}

		return render(request,'free.html',context)
	def post(self,request):
		OrderForm = FreeOrderForm(request.POST)

		if OrderForm.is_valid():
			OrderForm.save()
			return redirect('/')
		else:
			print(now())

		context = {
			'FreeOrderForm': OrderForm,
			'CurrentUser':request.user.id,
			'CurrentTime':now()
		}
		return render(request,'free.html',context)


class PremiumOrder(View):

	def get(self,request):
		OrderForm = PremiumOrderForm()
		context = {
			'PremiumOrderForm':OrderForm,
			'CurrentUser':request.user.id,
			'CurrentTime':now(),
		}

		return render(request,'buy.html',context)

	def post(self,request):
		OrderForm = PremiumOrderForm(request.POST)

		if OrderForm.is_valid():
			OrderForm.save()
			return redirect('/payment/process')
		else:
			print(now())

		context = {
			'PremiumOrderForm': OrderForm,
			'CurrentUser':request.user.id,
			'CurrentTime':now()
		}
		return render(request,'buy.html',context)

