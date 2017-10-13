from django.shortcuts import render
from django.http import HttpRequest
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse 
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def payment_done(request):
	return render(request,'done.html')


@csrf_exempt 
def payment_canceled(request):
	return render(request, 'canceled.html')


def payment_process(request):
	host = request.get_host()	
	paypal_dict = {
		'business':settings.PAYPAL_RECEIVER_EMAIL,
		'amount': 33,
		'currency_code' : 'USD',
		# 'notify_url' : 'http://{}{}'.format(host,reverse('paypal-ipn')),
		"notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
		'return_url' : 'http://{}{}'.format(host,reverse('payment:done')),
		'cancel_return' : 'http://{}{}'.format(host,reverse('payment:canceled')),
	}
	form = PayPalPaymentsForm(initial = paypal_dict)
	return render(request,'process.html',{'form':form})

