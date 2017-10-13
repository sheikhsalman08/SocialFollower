from django.db import models
from django.contrib import admin

from .models import Order
# Create your models here
admin.site.register(Order)