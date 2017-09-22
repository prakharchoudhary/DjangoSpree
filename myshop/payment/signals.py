from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order

def payment_notification(sender, **kwargs):
	ipn_onj = sender
	if ipn_onj.payment_status == ST_PP_COMPLETED:
		# payment was successful
		order = get_object_or_404(Order, id=ipn_onj.invoice)
		# mark the order as paid
		order.paid = True
		order.save()

valid_ipn_received.connect(payment_notification)