from __future__ import unicode_literals
from django.db import models


class Query(models.Model):
    content = models.CharField(max_length=511)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name.title()


class Snippet(models.Model):
    content = models.CharField(max_length=2047)
    created = models.DateField()
    updated = models.DateField()
    query = models.ForeignKey(Query)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "Response to query: '{}' on date: {}.".format(self.query, self.updated.strftime('%Y-%m-%d'))
