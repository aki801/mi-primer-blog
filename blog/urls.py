from django.conf.urls import include, url
from . import views

urlpatterns	= [
    url(r'^$', views.post_list),
]
#para decir que queremos que pase y quien lo va a hacer
