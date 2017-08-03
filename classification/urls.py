from django.conf.urls import url
from . import views

app_name = 'classification'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^check/$', views.CheckOK, name='check'),
    url(r'^results/$', views.results, name='results'),
]
