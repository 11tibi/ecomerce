from django import template

register = template.Library()


@register.filter(name='sub')
def sub(value, arg):
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return f'Sub invalid value value={value} arg={arg}'


@register.filter(name='addition')
def addition(value, arg):
    try:
        return float(value) + float(arg)
    except (ValueError, TypeError):
        return f'Addition invalid value value={value} arg={arg}'


@register.filter(name='smaller')
def smaller(value, arg):
    if arg is None:
        return False
    return float(value) > float(arg-0.50-0.30)


@register.filter(name='greater')
def greater(value, arg):
    if arg is None:
        return False
    return float(value) < float(arg-0.50+0.30)
