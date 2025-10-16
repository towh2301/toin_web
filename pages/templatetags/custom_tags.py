from django import template

register = template.Library()

@register.simple_tag
def is_locale_root(path):
    """
    Check if the given path is not the root path for any locale.
    """
    from django.conf import settings
    from django.utils.translation import get_language

    # Get the current language code
    current_language = get_language()

    # Construct the root path for the current locale
    locale_root_path = f'/{current_language}/'

    # Check if the given path is not the locale root path
    return path != locale_root_path and path != '/'
