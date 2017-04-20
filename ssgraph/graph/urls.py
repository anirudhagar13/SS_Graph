# howdy/urls.py
from django.conf.urls import url
from graph import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^ajax/debug_ajax/$', views.debug_ajax, name='debug_ajax'),
    url(r'^process_wordhash/$', views.process_wordhash, name='process_wordhash'),
    url(r'^process_synset/$', views.process_synset, name='process_synset'),
    url(r'^analyzepage/$', views.analyze_page, name='analyze_page'),
    url(r'^logspage/$', views.logs_page, name='logs_page'),
    url(r'^logreader/$', views.log_reader, name='log_reader'),
    url(r'^patentparser/$', views.patent_parser, name='patent_parser')
]
