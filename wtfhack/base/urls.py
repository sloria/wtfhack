"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns
from wtfhack.base.views import *


urlpatterns = patterns('wtfhack.base.views',
    url(r'^$', 'home', name='home'),
	url(r'^submit/$', 'submit', name='submit'),
    # ex: language/scala/
    url(r'^language/(?P<language>\w+)/$', get_repo, name='get_repo'),
)
