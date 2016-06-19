from django.conf.urls import url

from . import views

app_name = 'feed'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^user/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
 	url(r'^user/(?P<pk>[0-9]+)/feed/$', views.index_user, name='index_user'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<update_id>[0-9]+)/verify/$', views.verify, name='verify'),
    url(r'^update/$', views.post_update, name='post'),
]