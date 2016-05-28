from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^results/?$', views.search_result),
    url(r'^url/index/?$', views.indexing_url),
    url(r'^url/view/?$', views.editing_url),
    url(r'^status/?$', views.status),
    url(r'^about/?$', views.about),
]