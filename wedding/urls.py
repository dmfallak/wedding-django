from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^guests$', views.guests, name='guests'),
    url(r'^guests/([0-9]+)$', views.guests_by_id, name='guests_by_id'),
    url(r'^shuttle-froms$', views.shuttle_froms, name='shuttle_froms'),
    url(r'^shuttle-tos$', views.shuttle_tos, name='shuttle_tos'),
    url(r'^summaries$', views.summaries, name='summaries'),
    url(r'^guests-by-shuttle-from/([0-9]+)$', views.guests_by_shuttle_from_id, name='guests_by_shuttle_from_id'),
    url(r'^guests-by-shuttle-to/([0-9]+)$', views.guests_by_shuttle_to_id, name='guests_by_shuttle_to_id'),
    url(r'^shuttles$', views.shuttles, name='shuttles'),
]
