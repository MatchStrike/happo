from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404

from champion_manager.models import City, Champion

def city(request, slug=None):
	city = get_object_or_404(City, slug=slug)
	champions = city.champions.all()
	
	if city.hashtag:
		hashtag = city.hashtag.replace('#','')
	else:
		hashtag = 'happo'
	
	if not champions:
		raise Http404
	
	query_string = "+OR+".join(["%%23happo+from%%3A%s" % (x.screen_name,) for x in champions])
	query_url = "http://search.twitter.com/search.atom?q=%s" % (query_string,)
	
	return render_to_response('city.phtml',
			{'city':city,
			'hashtag':hashtag,
			'champions':champions,
			'query_url':query_url,
			}
			,context_instance=RequestContext(request))
	
