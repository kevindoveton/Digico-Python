from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^aux/(?P<auxnumber>[1-9]|1[0-2])/$', views.aux, name='aux'),
	url(r'^auxdata/(?P<auxnumber>[1-9]|1[0-2])/$', views.auxData, name='auxdata'),
	url(r'^auxupdate/$', views.auxUpdate, name='auxupdate'),
]
