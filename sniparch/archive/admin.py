from django.contrib import admin

from .models import Query, Tag, Snippet


admin.site.register(Query)
admin.site.register(Tag)
admin.site.register(Snippet)
