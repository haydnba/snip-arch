from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import QueryForm, TagForm, SnippetForm
from .models import Query, Tag, Snippet
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView


class SnippetCreate(CreateView):
    model = Snippet
    form_class = SnippetForm


class SnippetUpdate(UpdateView):
    model = Snippet
    form_class = SnippetForm


class SnippetDelete(DeleteView):
    model = Snippet
    success_url = reverse_lazy('snippet-list')


class SnippetList(ListView):
    model = Snippet


class SnippetDetail(DetailView):
    model = Snippet
