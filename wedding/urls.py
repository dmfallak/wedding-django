from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^guests$', views.guests, name='guests'),
    url(r'^guests/([0-9]+)$', views.guests_by_id, name='guests_by_id'),
]
