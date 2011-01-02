from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class City(models.Model):
	name = models.CharField('City', max_length=255, blank=False)
	slug = models.SlugField('URL', max_length=255, blank=False)
	hashtag = models.CharField('Hashtag', max_length=100, blank=True)
	
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField('Last Modified', auto_now=True, auto_now_add=False)
	
	def __unicode__(self):
		return self.name
		
	@models.permalink
	def get_absolute_url(self):
		return ('city', [self.slug])
		
class Champion(models.Model):
	screen_name = models.CharField('Twitter Screen Name', max_length=18, blank=False)
	cities = models.ManyToManyField(City, related_name='champions')
	
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField('Last Modified', auto_now=True, auto_now_add=False)
	
	def __unicode__(self):
		return self.screen_name