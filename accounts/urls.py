from django.conf.urls.defaults import *

from ducats.accounts import views

urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', views.account_detail, name='account_detail'),
)
