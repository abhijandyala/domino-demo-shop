"""Order service request handler. Synthetic demo code for Domino."""

from orders import inventory
from orders.pricing import price
from orders.validation import validate


def confirm(order):
    return {"status": "confirmed", "order_id": order.id}

def handle_order(request):
    order = validate(request)
    price(order)
    return confirm(order)
