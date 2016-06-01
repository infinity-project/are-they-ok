from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from feed import views

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
# 	url(r'^update/', login_required(views.UpdateView.as_view())),
]