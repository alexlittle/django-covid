# orb/analytics/urls.py
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^$', 'orb.analytics.views.home_view', name="orb_analytics_home"),
    url(r'^map/$', 'orb.analytics.views.map_view', name="orb_analytics_map"),
    url(r'^tag/(?P<id>\d+)/$', 'orb.analytics.views.tag_view', name="orb_analytics_tag"),
    url(r'^tag/(?P<id>\d+)/download/(?P<year>\d+)/(?P<month>\d+)/$', 'orb.analytics.views.tag_download', name="orb_analytics_download"),

)