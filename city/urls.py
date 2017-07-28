from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get-sub-setor/(?P<setor_id>[0-9]+)/$', views.get_subsetor, name='get_subsetor'),
]
