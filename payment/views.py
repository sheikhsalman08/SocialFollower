from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from Order.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import test

@login_required
@csrf_exempt
def payment_done(request):
    return render(request, 'done.html')


@login_required
@csrf_exempt
def payment_canceled(request):
    return render(request, 'canceled.html')

    
@login_required
def payment_process(request):
    # order_id = request.session.get('order_id')
    # order = get_object_or_404(Order, id=order_id)
    current_user_id = request.user.id
    host = request.get_host()
    order= Order.objects.filter(by_user = current_user_id).last()
<<<<<<< HEAD
    # print(order.id)
    # print(host)
=======
    print(order.id)
>>>>>>> b775cee5636e160ad176f7e505afa8b1133d6724

    paypal_dict = {
        # 'business': settings.PAYPAL_RECEIVER_EMAIL,
        # 'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        # 'invoice': str(order.id),
<<<<<<< HEAD
        'amount':"2",
        # 'item_name': str(order.id),
=======
        'amount':1,
>>>>>>> b775cee5636e160ad176f7e505afa8b1133d6724
        'item_name': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process.html', {'form':form})
