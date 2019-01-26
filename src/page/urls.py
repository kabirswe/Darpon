from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(
        r'^$',
        views.home,
        name='home'
    ),
    url(
        r'^project/$',
        views.project,
        name='project'
    ),
    url(
        r'^services/$',
        views.services,
        name='services'
    ),
    url(
        r'^team/$',
        views.team,
        name='team'
    ),
    url(
        r'^team-detail/$',
        views.team-detail,
        name='team-detail'
    ),
]
