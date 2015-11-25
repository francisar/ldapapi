from django.conf.urls import patterns, include, url

from django.contrib import admin
from ldapapi.ldapusermanage.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ldapapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^user/$',user),
    url(r'^admin/', include(admin.site.urls)),
)
