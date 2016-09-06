Django CMS Integration
======================

Imagestore can show an album as a plugin in django-cms, and can be used as a django-cms app.

To use plugins, just add `imagestore.imagestore_cms` to your `INSTALLED_APPS`

If you want to use imagestore as a django-cms application

* Set `IMAGESTORE_SHOW_USER` to `False`
* Because django-cms build connect apps without namespace settings
  you need to tell django where to search imagestore namespace,
  you can do it by adding django-cms urls with the 'imagestore' namespace::

    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore'))
