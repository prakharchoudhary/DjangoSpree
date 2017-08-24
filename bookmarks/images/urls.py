from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^create/$', views.image_create, name='create'),
	url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
	url(r'^like/$', views.image_like, name='like'),
]