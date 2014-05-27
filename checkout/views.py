from oscar.apps.checkout.views import PaymentMethodView as BasePaymentMethodView
from django import http
from django.core.urlresolvers import reverse

class PaymentMethodView(BasePaymentMethodView):
 
    def get(self, request, *args, **kwargs):
        # By default we redirect straight onto the payment details view. Shops
        # that require a choice of payment method may want to override this
        # method to implement their specific logic.
        return self.get_success_response()

    def get_success_response(self):
        return http.HttpResponseRedirect(reverse('checkout:preview'))

