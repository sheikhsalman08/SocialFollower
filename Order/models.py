from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime, timedelta


# Create your models here.

class Order(models.Model):
	by_user = models.ForeignKey(User, blank = True, null = True, related_name="owner")
	time = models.DateTimeField(blank = True, null = True)		#format 2012-01-01 00:00:00
	amount = models.IntegerField(blank = True, null = True)
	choices = (
	(u'1',u'instagram'),
	(u'2',u'facebook'),
	(u'3',u'youtube'),
	# ('1','Instagram'),('2','facebook'),('3','youtube')
	 )
	type = models.CharField(max_length = 230,default = "Did Not Put",blank = True, null = True, choices = choices)
	order_social_site_user_name = models.CharField(max_length = 30, blank = True, null = True,default = "")
	order_social_site_url = models.CharField(max_length = 100, blank = True, null = True,default = "")
	payment_status = models.NullBooleanField(blank = True, null = True,default=True)	#edit this line at asana
	visibility_by_admin = models.BooleanField(blank = True, default=True)	#edit this line at asana		
	
	def __str__(self,*args,**kwargs):
		return "By {} in {} at {}".format(self.by_user, self.type, self.time.date())


		# return datetime.strptime('2014-2-2', '%Y-%m-%d').date()

	def save(self, *args, **kwargs):
		if (self.time is None):
			self.time = now() + timedelta(hours=8)		# for malaysian time
		if (self.amount is None):
			self.amount = 0

		super(Order, self).save(*args, **kwargs)