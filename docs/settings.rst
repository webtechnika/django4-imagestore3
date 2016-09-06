Available settings
==================

IMAGESTORE_UPLOAD_TO ("imagestore/")
    Path for uploading images

IMAGESTORE_IMAGES_ON_PAGE (20)
    Number of images in one page (album/user/tag view)

IMAGESTORE_ON_PAGE (20)
    Number of albums on page (index view)

IMAGESTORE_SELF_MANAGE (True)
    If true, imagestore install handler on launch, that grant add/change/delete
    permissions for Album and Image models for every created user (with this permissions
    users can create personal galleries, if you don't want it set this settings to False).

IMAGESTORE_TEMPLATE ("base.html")
    Here you can set template that imagestore templates will inhert.
    Imagestore templates expect next blocks in basic template:
    
        * head (inside <head> tag for scripts and styles inserting)
        * title (inside <tilte> tag)
        * breadcrumb
        * content (main content)
        * content-related (this block used for tag-cloud, user info and create/edit links)

IMAGESTORE_SHOW_USER (True)
    Show user info (such as avatar, link to profile and other stuff)
    Default template expects that profile has avatar ImageField and get_absolute_url method
    You can customize view it by overriding `imagestore/user_info.html` template

    Notice, that since imagestore version 2.7.4, which supports custom user model,
    in `imagestore/user_info.html` passes `user` variable with current logged in user.

IMAGE_MODEL ("imagestore.models.Image")
    Class for storing images. See :doc:`extending imagestore <extending>` for details.

ALBUM_MODEL ("imagestore.models.Album")
    Class for storing albums. See :doc:`extending imagestore <extending>` for details.

IMAGESTORE_IMAGE_FORM ("imagestore.forms.ImageForm")
    Form for uploading images. See :doc:`extending imagestore <extending>` for details.

IMAGESTORE_ALBUM_FORM ("imagestore.forms.AlbumForm")
    Form for creating albums. See :doc:`extending imagestore <extending>` for details.

IMAGESTORE_LOAD_CSS ("True")
    Load CSS file 'static/imagestore.css' in imagestore templates. If you want to use custom theme - disable this settings.

IMAGESTORE_UPLOAD_ALBUM_PROCESSOR ("imagestore.models.upload.process_zipfile")
    Function for processing uploaded zip archives from admin interface. Function gets `AlbumUpload` model instance
    and should process file from `zip_file` field to upload images. For example, you can override this setting
    to provide function, which do nothing, and process file lately

IMAGESTORE_BRIEF_TO_ALT_TEMPLATE ("{0}_{1}")
    There is template tag `imagestore_alt` which automaticly generates images
    alt attribute based on image title or, if title is empty, on album brief
    field and (optional) loop counter. Setting determines alt attribute format
    when brief ({0}) and counter ({1}) are used.
