from django.core.files.base import ContentFile
from django.db import models
from django.db.models.functions import Coalesce
from django.db.models import Sum, F
import math
import decimal
from django.db.models import Sum, Subquery, F, OuterRef, DecimalField, Value, IntegerField, Max

import uuid
from urllib.parse import urlparse
import os
import os.path
import random
from django.conf import settings
from django.core.files import File


from django.db import models
from django.utils.text import slugify


class Museum(models.Model):

    class MuseumType(models.TextChoices):
        ART             = 'art',             'Art'
        HISTORY         = 'history',         'History'
        NATURAL_HISTORY = 'natural_history', 'Natural History'
        SCIENCE         = 'science',         'Science'
        TRANSPORT       = 'transport',       'Transport'
        ANTHROPOLOGY    = 'anthropology',    'Culture & Anthropology'
        OTHER           = 'other',           'Other'

    # Identity
    name        = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)
    type        = models.CharField(max_length=50, choices=MuseumType.choices, default=MuseumType.OTHER)
    description = models.TextField(blank=True)
    # image       = models.ImageField(upload_to='museums/', blank=True, null=True)

    # Location
    city        = models.CharField(max_length=100)
    country     = models.CharField(max_length=100)
    address     = models.CharField(max_length=255, blank=True)

    # Info
    founded_year    = models.PositiveSmallIntegerField(blank=True, null=True)
    director        = models.CharField(max_length=150, blank=True)
    website         = models.URLField(blank=True)
    admission       = models.CharField(max_length=150, blank=True,
                                       help_text='e.g. "Free" or "£22 adults"')
    opening_hours   = models.TextField(blank=True,
                                       help_text='Free-text opening hours description')
    collection_size = models.CharField(max_length=50, blank=True,
                                       help_text='e.g. "8M+" — display string')

    # Stats (denormalised for fast display)
    viewer_count    = models.PositiveIntegerField(default=0)
    average_rating  = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} · {self.city}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Exhibition(models.Model):

    class Status(models.TextChoices):
        CURRENT  = 'current',  'Current'
        NEW      = 'new',      'New'
        ARCHIVED = 'archived', 'Archived'

    class Category(models.TextChoices):
        ART          = 'art',          'Art'
        HISTORY      = 'history',      'History'
        ARCHAEOLOGY  = 'archaeology',  'Archaeology'
        SCIENCE      = 'science',      'Science'
        ANTHROPOLOGY = 'anthropology', 'Anthropology'
        RELIGION     = 'religion',     'Religion'
        PHOTOGRAPHY  = 'photography',  'Photography'
        OTHER        = 'other',        'Other'

    # Identity
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)
    museum      = models.ForeignKey(Museum, on_delete=models.CASCADE,
                                    related_name='exhibitions')
    category    = models.CharField(max_length=50, choices=Category.choices,
                                   default=Category.OTHER)
    tags        = models.ManyToManyField(Tag, blank=True, related_name='exhibitions')
    status      = models.CharField(max_length=20, choices=Status.choices,
                                   default=Status.CURRENT)

    # Content
    description     = models.TextField(blank=True)
    duration_minutes = models.PositiveSmallIntegerField(
        default=30,
        help_text='Estimated viewing time in minutes'
    )
    # image           = models.ImageField(upload_to='exhibitions/', blank=True, null=True)

    # Stats
    viewer_count    = models.PositiveIntegerField(default=0)
    average_rating  = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    age_range   = models.CharField(max_length=50, blank=True,
                                 help_text='e.g. "All ages", "Kids", "Adults"')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} — {self.museum.name}'

    @property
    def duration_display(self):
        """Returns e.g. '45 min' or '1 hr 20 min'."""
        h, m = divmod(self.duration_minutes, 60)
        if h:
            return f'{h} hr {m} min' if m else f'{h} hr'
        return f'{m} min'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)