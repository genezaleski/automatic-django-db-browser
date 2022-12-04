from django import template

register = template.Library()

@register.filter(name="returnitem")
def return_item(l,i):
	try:
		return l[i]
	except: 
		return None
