"""Defines url patterns for learning_logs."""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Base page
    url(r'^base$', views.base, name='base'),

    # Base_bak page
    url(r'^base_bak$', views.base_bak, name='base_bak'),

    # Home page
    url(r'^$', views.index, name='index'),

    # About page
    url(r'^about/$', views.about, name='about'),

    # Topics page: shows all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # New topic form page
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # New entry page: allows user to add a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    # Markdown cheatsheet page
    url(r'^md_cheatsheet/$', views.md_cheatsheet, name='md_cheatsheet'),

]