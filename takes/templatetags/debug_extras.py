from django import template

register = template.Library()


@register.filter
def dict_key(d, k):
    """Returns the given key from a dictionary."""
    # this is only needed because form errors uses __all__ but . notation can't access _ property
    return d[k]


@register.simple_tag
def debug_object_dump(var):
    print(var)
    # type of var
    print(type(var))

    print('+++++++')

    # if var is a dict print all its elements
    if isinstance(var, dict):
        for key, value in var.items():
            print(key + ' :')
            print(value)
            print(type(value))
            print('----')

    return ""
