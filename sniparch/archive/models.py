from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class Query(models.Model):
    query_string = models.CharField(max_length=511)
    search_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['search_date', 'id']
        get_latest_by = 'search_date'

    def __str__(self):
        return "{} on {} (id = {}).".format(
        self.query_string, self.search_date.strftime('%Y-%m-%d'), self.id
        )

    def get_absolute_url(self):
        return reverse(
            'archive_query_detail',
            kwargs={'id': self.id}
        )


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse(
            'archive_tag_detail',
            kwargs={'slug': self.slug}
        )

    # def set_slug(self):
    #     self.slug = "-".join(self.cleaned_data['name'].lower().split())


class Snippet(models.Model):
    question = models.ForeignKey(Query)
    answer = models.CharField(max_length=2047)
    source = models.URLField(max_length=255, blank=True)
    created = models.DateTimeField('Date Created', auto_now_add=True)
    updated = models.DateTimeField('Last Modified', auto_now=True)
    # slug = models.SlugField()
    tags = models.ManyToManyField(Tag, related_name='snippets')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return "Response to query: '{}', on date: {}.".format(
            self.question, self.updated.strftime('%Y-%m-%d')
        )

    def get_absolute_url(self):
        return reverse(
            'archive_snippet_detail',
            kwargs={'slug': self.slug}
        )
