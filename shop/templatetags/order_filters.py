from django import template
from decimal import Decimal

register = template.Library()


@register.filter
def sum_total(orders):
    """Calculate total revenue from all orders"""
    return sum(order.total_amount for order in orders)


@register.filter
def avg_total(orders):
    """Calculate average order value"""
    if orders.count() == 0:
        return 0
    total = sum(order.total_amount for order in orders)
    return round(total / orders.count(), 2)


@register.filter
def multiply(value, arg):
    """Multiply two values"""
    try:
        return Decimal(str(value)) * Decimal(str(arg))
    except:
        return 0
