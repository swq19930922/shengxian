from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add/(\d+)/(\d+)/$', views.add_goods, name='add_goods'),
    url(r'^delete/(\d+)/$', views.delete_goods, name='delete_goods'),
    url(r'^edit/(\d+)/(\d+)/$', views.edit_goods, name='edit_goods'),
]