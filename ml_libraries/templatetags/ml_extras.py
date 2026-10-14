from django import template
import json

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Get item from dictionary using key."""
    return dictionary.get(key)


@register.filter
def get_by_slug(queryset, slug):
    """Get object from queryset by slug."""
    for obj in queryset:
        if obj.slug == slug:
            return obj
    return None


@register.filter
def json_script(value, prefix):
    """Output JSON for use in script tags."""
    return json.dumps(value)


@register.filter
def mul(value, arg):
    """Multiply two numbers."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def div(value, arg):
    """Divide two numbers."""
    try:
        return float(value) / float(arg) if float(arg) != 0 else 0
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


@register.filter
def sub(value, arg):
    """Subtract arg from value."""
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def add(value, arg):
    """Add two numbers."""
    try:
        return float(value) + float(arg)
    except (ValueError, TypeError):
        return 0