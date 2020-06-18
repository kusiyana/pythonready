from django import template
register = template.Library()

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the value of key (k) from a dictionary (d).'''
    return d.get(k)
