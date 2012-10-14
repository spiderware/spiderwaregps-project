#-*- coding: utf-8 -*-
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = "static"
        super(StaticStorage, self).__init__(*args, **kwargs)


class MediaStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = "media"
        super(MediaStorage, self).__init__(*args, **kwargs)


class FilerMediaStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = "media/filer"
        super(FilerMediaStorage, self).__init__(*args, **kwargs)


class FilerMediaThumbnailStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = "media/filer_thumbnails"
        super(FilerMediaThumbnailStorage, self).__init__(*args, **kwargs)