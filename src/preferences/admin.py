""" Admin for the Preferences app """

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from image_cropping import ImageCroppingMixin
from import_export.admin import ImportExportMixin

from . import models


class EmailsInline(admin.TabularInline):
    model = models.Emails
    extra = 0
    exclude = ['created_by', 'updated_by', ]

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
        obj.save()


class FaxsInline(admin.TabularInline):
    model = models.Faxs
    extra = 0
    exclude = ['created_by', 'updated_by', ]

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
        obj.save()


class PhoneInline(admin.TabularInline):
    model = models.Phone
    extra = 0
    exclude = ['created_by', 'updated_by', ]

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
        obj.save()


class TelePhoneInline(admin.TabularInline):
    model = models.TelePhone
    extra = 0
    exclude = ['created_by', 'updated_by', ]

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
        obj.save()


class AddressInline(admin.TabularInline):
    model = models.Address
    extra = 0
    exclude = ['created_by', 'updated_by', ]

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
        obj.save()


# Register your models here.
@admin.register(models.Preference)
class PreferenceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [
        EmailsInline,
        FaxsInline,
        PhoneInline,
        TelePhoneInline,
        AddressInline,
    ]
    list_display = (
        'title',
        'logo',
        'logo_cropping',
        'created_on',
    )
    readonly_fields = (
        'id',
        'created_on',
    )


@admin.register(models.Page)
class PageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'created_on',
    )
    readonly_fields = (
        'id',
        'created_on',
        'updated_on',
        'slug',
    )


@admin.register(models.PageText)
class PageTextAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'heading',
        'page',
        'created_on',
    )
    readonly_fields = (
        'id',
        'created_on',
        'updated_on',
    )
    list_per_page = 30
    list_filter = (
        'page',
    )
    list_display_links = (
        'heading',
        'page',
    )
    search_fields = (
        'heading',
        'page',
    )
