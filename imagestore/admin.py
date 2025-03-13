from __future__ import unicode_literals

import logging

import swapper
from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminInlineImageMixin
from sorl.thumbnail.helpers import ThumbnailError

from .models.album import Album
from .models.image import Image
from .models.upload import AlbumUpload

logger = logging.getLogger(__name__)


class InlineImageAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = Image
    fieldsets = ((None, {'fields': ['image', 'user', 'title', 'order', 'tags', 'album']}),)
    raw_id_fields = ('user', )
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['name', 'brief', 'user', 'is_public', 'order']}),)
    list_display = ('name', 'admin_thumbnail', 'user', 'created', 'updated', 'is_public', 'order')
    list_editable = ('order', )
    inlines = [InlineImageAdmin]

    def admin_thumbnail(self, obj):
        img = obj.get_head()
        if not img:
            return _('Empty album')

        try:
            thumb = get_thumbnail(img.image, '100x100', crop='center')
            return mark_safe('<img src="{}" alt="">'.format(thumb.url))
        except (IOError, ThumbnailError):
            logger.info('Can\'t crate thumbnail from image {}'.format(img),
                        exc_info=settings.DEBUG)
            return ''

    admin_thumbnail.allow_tags = True


class ImageAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['user', 'title', 'image', 'description', 'order', 'tags', 'album']}),)
    list_display = ('admin_thumbnail', 'user', 'order', 'album', 'title', 'width', 'height')
    raw_id_fields = ('user', )
    list_filter = ('album', )

    def admin_thumbnail(self, obj):
        try:
            thumb = get_thumbnail(obj.image, '100x100', crop='center')
            return mark_safe('<img src="{}" alt="">'.format(thumb.url))
        except (IOError, ThumbnailError):
            logger.info('Can\'t crate thumbnail from image {}'.format(self),
                        exc_info=settings.DEBUG)
            return ''

    admin_thumbnail.allow_tags = True

    def width(self, obj):
        try:
            return obj.image.width
        except IOError:
            return None

    def height(self, obj):
        try:
            return obj.image.height
        except IOError:
            return None


class AlbumUploadAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


if not swapper.is_swapped('imagestore', 'Image'):
    admin.site.register(Image, ImageAdmin)

if not swapper.is_swapped('imagestore', 'Album'):
    admin.site.register(Album, AlbumAdmin)
    admin.site.register(AlbumUpload, AlbumUploadAdmin)
