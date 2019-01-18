""" Models for the Preferences app """
from __future__ import unicode_literals

import uuid

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField
from ckeditor_uploader.fields import RichTextUploadingField
# from phonenumber_field.modelfields import PhoneNumberField
from geoposition.fields import GeopositionField


# Functions
def logo_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return "preference/%s/%s" % (
        timezone.now().strftime('%Y/%m/%d'),
        filename
    )


# Create your models here.
class Preference(models.Model):

    # Attributes
    title = models.CharField(
        _('title'),
        max_length=40,
        unique=True,
    )
    note = RichTextUploadingField(
        _('note'),
        blank=True,
        null=True,
    )
    logo = models.ImageField(
        _('logo'),
        upload_to=logo_upload_to
    )
    logo_cropping = ImageRatioField(
        'logo',
        '1600x900'
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['title']
        verbose_name = _('Preference')
        verbose_name_plural = _('Preferences')

    # Functions
    def __str__(self):
        return "%s" % (self.title)

    def __unicode__(self):
        return u"%s" % (self.title)

    def list_image_url(self):
        if self.logo:
            return get_thumbnailer(self.logo).get_thumbnail({
                'size': (280, 240),
                'box': self.logo_cropping,
                'crop': True,
                'detail': True,
            }).url


class Emails(models.Model):

    # Relations
    preference = models.ForeignKey(
        'Preference',
        verbose_name=_('Preference'),
    )

    # Attributes
    email = models.EmailField(
        _('email'),
        max_length=40,
        unique=True,
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['email']
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    # Functions
    def __str__(self):
        return "%s" % (self.email)

    def __unicode__(self):
        return u"%s" % (self.email)


class Faxs(models.Model):

    # Relations
    preference = models.ForeignKey(
        'Preference',
        verbose_name=_('Preference'),
    )

    # Attributes
    fax = models.CharField(
        _('fax'),
        max_length=40,
        unique=True,
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['fax']
        verbose_name = _('Fax')
        verbose_name_plural = _('Faxes')

    # Functions
    def __str__(self):
        return "%s" % (self.fax)

    def __unicode__(self):
        return u"%s" % (self.fax)


class Phone(models.Model):

    # Relations
    preference = models.ForeignKey(
        'Preference',
        verbose_name=_('Preference'),
    )

    # Attributes
    phone = models.CharField(
        _('phone number'),
        max_length=40,
        blank=True,
        null=True
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')

    # Functions
    def __str__(self):
        return "%s" % (self.phone)

    def __unicode__(self):
        return u"%s" % (self.phone)


class TelePhone(models.Model):

    # Relations
    preference = models.ForeignKey(
        'Preference',
        verbose_name=_('Preference'),
    )

    # Attributes
    telephone = models.CharField(
        _('telephone number'),
        max_length=40,
        blank=True,
        null=True
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        verbose_name = _('TelePhone')
        verbose_name_plural = _('TelePhones')

    # Functions
    def __str__(self):
        return "%s" % (self.telephone)

    def __unicode__(self):
        return u"%s" % (self.telephone)


class Address(models.Model):

    # Relations
    name = models.CharField(
        _('name'),
        max_length=40,
        unique=True,
    )
    preference = models.ForeignKey(
        'Preference',
        verbose_name=_('Preference'),
    )

    # Attributes
    fullAddress = RichTextUploadingField(
        _('fullAddress'),
        blank=True,
        null=True,
    )
    address = GeopositionField(
        _('address'),
        blank=True,
        null=True,
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    # Functions
    def __str__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return u"%s" % (self.name)


class Page(models.Model):
    name = models.CharField(
        _('name'),
        max_length=200,
    )
    slug = models.SlugField(
        _('slug'),
        max_length=206,
        unique=True,
    )

    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['name']
        verbose_name = _('page')
        verbose_name_plural = _('pages')

    # Functions
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)
        self.slug = '-'.join((slugify(self.id), slugify(self.name)))
        return super(Page, self).save(*args, **kwargs)


class PageText(models.Model):

    # Relations
    page = models.ForeignKey(
        'Page',
        verbose_name=_('Pages'),
    )
    # Attributes
    heading = models.CharField(
        _('heading'),
        max_length=200,
        blank=True,
        null=True,
    )
    content = RichTextUploadingField(
        _('content'),
        blank=True,
        null=True,
    )
    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        verbose_name = _('Page Text')
        verbose_name_plural = _('Page Text')
