from django import template

register = template.Library()


@register.filter(name='sub')
def sub(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
