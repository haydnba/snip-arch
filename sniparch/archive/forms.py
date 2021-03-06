from django.forms import ModelForm

from .models import Query, Tag, Snippet


class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ['question']
