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
]
