from oscar.apps.shipping import repository
from . import methods


class Repository(repository.Repository):
    # Available Shipping methods
    # methods[0] – default method
    methods = (methods.StandardTakeAway(),
               methods.Standard(),
               methods.TakeAwayBoxberry(),
               methods.Boxberry())

    '''
    # Select method with condition
    def get_available_shipping_methods(
            self, basket, user=None, shipping_addr=None,
            request=None, **kwargs):
        methods = (methods.Standard())
        if shipping_addr and shipping_addr.country.code == 'GB':
            # Express is only available in the UK
            methods = (methods.Standard(), methods.Express())
        return methods
    '''