from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, DetailView

from .forms import QueryForm, TagForm, SnippetForm
from .models import Query, Tag, Snippet


class IndexPage(CreateView):
    model = Query
    form_class = QueryForm
    template_name = 'archive/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        context['snippet_list'] = Snippet.objects.all()
        return context

class QueryCreate(CreateView):
    model = Query
    form_class = QueryForm
    template_name = 'archive/query_form.html'


class QueryList(ListView):
    model = Query
    template_name = 'archive/query_list.html'


class TagCreate(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'archive/tag_form.html'


class TagList(ListView):
    model = Tag
    template_name = 'archive/tag_list.html'


class SnippetCreate(CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'archive/snippet_form.html'


# class SnippetUpdate(UpdateView):
#     model = Snippet
#     form_class = SnippetForm
#     template_name = 'archive/snippet_form.html'
#
#
# class SnippetDelete(DeleteView):
#     model = Snippet
#     success_url = reverse_lazy('snippet-list')


class SnippetList(ListView):
    model = Snippet
    template_name = 'archive/snippet_list.html'


# class SnippetDetail(DetailView):
#     model = Snippet
#     template_name = 'archive/snippet_detail.html'
