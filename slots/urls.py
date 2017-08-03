from django.conf.urls import url
from . import views

app_name = 'slots'      # namespacing url names for templates
urlpatterns = [
    url(r'^$', views.SlotView.as_view(), name='slot_view'),
    url(r'^submit/$', views.SubmitView, name='submit'),
    url(r'^done/$', views.DoneView, name='done'),
]
