from django import template

register = template.Library()


@register.simple_tag
def multiply(price, quantity):
    return float(price) * float(quantity)
