from django.db import models
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received

# Create your models here.

def show_me_the_money(sender, **kwargs):
    print('hi')

valid_ipn_received.connect(show_me_the_money)


def show_me_the_money2(sender, **kwargs):
    print('hi')

invalid_ipn_received.connect(show_me_the_money2)

# from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

# @receiver(valid_ipn_received)
# def show_me_the_money(sender, **kwargs):
#     """Do things here upon a valid IPN message received"""
#     ...

# @receiver(invalid_ipn_received)
# def do_not_show_me_the_money(sender, **kwargs):
#     """Do things here upon an invalid IPN message received"""
#     ...