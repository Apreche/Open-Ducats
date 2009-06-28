from django.conf.urls.defaults import *

from accounts import views,models

urlpatterns = patterns('',
    (r'^(?P<slug>[-\w]+)/$', views.account_detail),
)
