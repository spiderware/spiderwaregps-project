#-*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.contrib.gis.measure import D


class RawFile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    file = models.FileField(blank=True)


class Track(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=True, default='', max_length=255)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    raw_source = models.ForeignKey(RawFile, null=True, blank=True, on_delete=models.SET_NULL)


class TrackItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    track = models.ForeignKey(Track)
    when = models.DateTimeField()
    location = models.PointField(null=True, blank=True)

    objects = models.GeoManager()

    class Meta:
        get_latest_by = 'when'

    def __unicode__(self):
        return u"track %s %s %s" % (self.track_id, self.when, self.location)