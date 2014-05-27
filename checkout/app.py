from oscar.apps.checkout.app import CheckoutApplication as CoreCheckoutApplication
from .views import PaymentMethodView

class CheckoutApplication(CoreCheckoutApplication):
  payment_method_view = PaymentMethodView

application = CheckoutApplication()
