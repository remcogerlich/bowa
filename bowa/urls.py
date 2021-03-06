# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from bowa import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^ui/', include('lizard_ui.urls')),
    url(r'^map/', include('lizard_map.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.HomeView.as_view(),
        name='bowa_homepage'),
    url(r'^disclaimer$', views.Disclaimer.as_view()),

    url(
        r'^result/(?P<slug>[^/]*)/$',
        views.BowaScenarioResult.as_view(),
        name='bowa_result'
    ),
    url(
        r'^result/(?P<slug>[^/]*)/map/$',
        views.BowaScenarioResultMap.as_view(),
        name='bowa_result_map'
    ),
    url(
        r'^result/(?P<slug>[^/]*)/graph/$',
        views.BowaScenarioResultGraph.as_view(),
        name='bowa_result_graph'
    ),
    url(
        r'^result/(?P<slug>[^/]*)/graph/image/$',
        views.result_graph_image,
        name='bowa_result_graph_image'
    ),
    url(
        r'^result/(?P<slug>[^/]*)/kml/$',
        views.ResultKML.as_view(),
        name='bowa_result_kml'
    ),
)

urlpatterns += debugmode_urlpatterns()
