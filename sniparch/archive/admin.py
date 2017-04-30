from django.contrib import admin

from .models import Query, Tag, Snippet


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Query)
admin.site.register(Tag, TagAdmin)
admin.site.register(Snippet)
