from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
# import weasyprint
from io import BytesIO
from Order.models import Order
from .models import test

def payment_notification(sender, **kwargs):
    ipn_obj = sender
    order_id = ipn_obj.item_name
    order = Order.objects.get(id = order_id)
    order.payment_status = True
    print(ipn_obj.item_name)
    order.save()

valid_ipn_received.connect(payment_notification)




# def payment_notification(sender, **kwargs):
#     ipn_obj = sender
#     if ipn_obj.payment_status == ST_PP_COMPLETED:
#         # payment was successful
#         order = get_object_or_404(Order, id=ipn_obj.invoice)

#         # mark the order as paid
#         order.paid = True
#         order.save()

#         # create invoice e-mail
#         subject = 'My Shop - Invoice nr. {}'.format(order.id)
#         message = 'Please, find attached the invoice for your recent purchase.'
#         email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])

#         # generate PDF
#         html = render_to_string('orders/order/pdf.html', {'order': order})
#         out = BytesIO()
#         # stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
#         # weasyprint.HTML(string=html).write_pdf(out,
#                                                # stylesheets=stylesheets)
#         # attach PDF file
#         email.attach('order_{}.pdf'.format(order.id),
#                      out.getvalue(),
#                      'application/pdf')
#         # send e-mail
#         email.send()
