from django.shortcuts import get_object_or_404
from accounts.models import Customer

def orderCount(request):
    """ 
    Used as an if statement in the base.html
    file to alternate the page based on whether
    you have made any orders or not.
    """
    if request.user.is_authenticated:
        try: 
            customer = Customer.objects.get(user=request.user)
            orders = customer.order_set.all()
            order_count = orders.count()
        except Customer.DoesNotExist:
            order_count = None
    else:
        order_count = None
    return {'order_count': order_count}