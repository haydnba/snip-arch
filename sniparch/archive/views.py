from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SnippetForm
from .models import Query, Tag, Snippet
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView


class SnippetCreate(CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = "snippet_form.html"


class SnippetUpdate(UpdateView):
    model = Snippet
    form_class = SnippetForm
    template_name = "snippet_form.html"


class SnippetDelete(DeleteView):
    model = Snippet
    success_url = reverse_lazy('snippet-list')


class SnippetList(ListView):
    model = Snippet
    template_name = "snippet_list.html"


class SnippetDetail(DetailView):
    model = Snippet
    template_name = "snippet_detail.html"
