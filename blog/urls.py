from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.homepage, name='homepage'),
     url(r'^about/', views.about, name='about'),
     url(r'^products/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
     url(r'^products/$', views.products, name='products'),
     url(r'^', views.err, name='err'),

]
