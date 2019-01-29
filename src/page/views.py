from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import template
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, EmailMessage
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from urllib import urlencode

from preferences.models import PageText


__author__ = 'Alamgir Kabir Roni'
__copyright__ = 'Copyright 2018, Darpon Technology'


def home(request):
    context = {
        'nav': 'home',
    }
    return render(request, 'page/home.html', context)


def services(request):
    context = {
        'nav': 'services',
    }
    return render(request, 'page/services.html', context)


def team(request):
    context = {
        'nav': 'team',
    }
    return render(request, 'page/team.html', context)


def project(request):
    context = {
        'nav': 'project',
    }
    return render(request, 'page/project.html', context)


def team_detail(request):
    context = {
        'nav': 'team_detail',
    }
    return render(request, 'page/team_detail.html', context)


def contact(request):
    context = {
        'nav': 'contact',
    }
    return render(request, 'page/contact.html', context)


def contact_detail(request):
    context = {
        'nav': 'contact_detail',
    }
    return render(request, 'page/contact_detail.html', context)


def process(request):
    context = {
        'nav': 'process',
    }
    return render(request, 'page/process.html', context)
