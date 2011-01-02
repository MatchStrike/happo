from django import template

register = template.Library()

class get_cities(template.Node):
	def __init__(self, *args, **kwargs):
		pass
		
	def render(self, context):
		from champion_manager.models import City		
		context['cities'] = City.objects.exclude(champions=None).order_by('name')
		return ''
		
register.tag(get_cities)