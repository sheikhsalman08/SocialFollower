from django import forms
from .models import Order

class FreeOrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(FreeOrderForm, self).__init__(*args, **kwargs)
		self.fields['type'].widget.attrs\
			.update({
			'id':'buyer-input',
		})
		self.fields['order_social_site_user_name'].widget.attrs\
			.update({
			'id':'buyer-input',
		})
		self.fields['order_social_site_url'].widget.attrs\
			.update({
			'id':'buyer-input',
		})
		self.fields['visibility_by_admin'].widget.attrs\
			.update({
			'id':'buyer-input',
		})

class PremiumOrderForm(forms.ModelForm):
	class Meta:
			model = Order
			fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PremiumOrderForm, self).__init__(*args, **kwargs)

		self.fields['type'].widget.attrs\
		.update({
		'id':'buyer-input',
		})
		self.fields['order_social_site_user_name'].widget.attrs\
		.update({
		'id':'buyer-input',
		})
		self.fields['order_social_site_url'].widget.attrs\
		.update({
		'id':'buyer-input',
		})
		self.fields['visibility_by_admin'].widget.attrs\
		.update({
		'id':'buyer-input',
		})
		