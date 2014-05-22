from decimal import Decimal as D
from oscar.apps.shipping import repository, methods as core_methods

class Repository(repository.Repository):
  methods = [core_methods.FixedPrice(D('40.00'))]

  def get_shipping_methods(self, user, basket, shipping_addr=None, **kwargs):
    return self.prime_methods(basket, self.methods)

  def find_by_code(self, code, basket):
    for method in self.methods:
      if code == method.code:
        return self.prime_method(basket, method)

