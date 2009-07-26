from django.conf.urls.defaults import *

from ducats.transactions import views

urlpatterns = patterns('',
    url(r'^$', views.template_list, name='template_list'),
    url(r'(?P<template>[-\w]+)/$', views.transaction_log, name='transaction_log'),
)
