from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'tags/lista.html'
    context_object_name = 'tags'

