from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get an item from a dictionary using the key."""
    if dictionary is None:
        return 0
    return dictionary.get(str(key) if isinstance(key, int) else key, 0)
