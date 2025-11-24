from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/lista.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DeleteView):
    model = Post
    template_name = 'posts/detalhe.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/formulario.html'
    fields = ['titulo', 'conteudo', 'slug', 'tags']
    success_url = reverse_lazy('posts:lista')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/formulario.html'
    fields = ['titulo', 'conteudo', 'slug', 'tags']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('posts:lista')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/confirmar_deletar_post.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('posts:lista')
