from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^list/(\d+)/^$', views.goodslist, name='goodslist')
    url(r'^list/(\d+)/(\d+)/(\d+)/$', views.goodslist, name='goodslist'),
    url(r'^(\d+)/$', views.detail, name='detail'),
]