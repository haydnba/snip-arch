from __future__ import unicode_literals
from django.db import models


class Query(modesl.Model)
    content = models.CharField(max_length=511)

    def __str__(self):
        return self.content


class Tag(models.Model)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Snippet(models.Model)
    content = models.CharField(max_length=2047)
    created = models.DateField()
    updated = models.DateField()
    query = models.ForeignKey(Query)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        pass
