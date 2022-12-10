from django import template

register = template.Library()

@register.filter(name="returnitem")
def return_item(l,i):
	try:
		return l[i]
	except: 
		return None

@register.filter(name="returnkeys")
def return_keys(l):
	return l.keys()

@register.simple_tag
def define(val=None):
	return val
