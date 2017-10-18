from django.db import models

# Create your models here.

class test(models.Model):
	amount = models.IntegerField(blank = True, null = True)
	status = models.CharField(max_length = 22, default = "Not", blank = True, null = True)


