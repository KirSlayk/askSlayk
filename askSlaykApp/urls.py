from django.conf.urls import patterns, url

from /home/leegheid/askSlayk/askSlaykApp import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
}
