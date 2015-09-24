from django.conf.urls import include, url
from . import views

urlpatterns	= [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]
#para decir que queremos que pase y quien lo va a hacer
