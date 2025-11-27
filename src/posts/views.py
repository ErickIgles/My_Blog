from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, View, ListView, DetailView
from django.contrib import messages

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/lista.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().filter(autor=self.request.user)\
            .select_related('autor')\
            .prefetch_related('tags')
        return qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detalhe.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/formulario.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:lista')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "Post criado com sucesso.")
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/formulario.html'
    form_class = PostForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('posts:lista')
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.autor != request.user:
            messages.error(request, 'Você não tem permissão para acessar ou editar este post.')
            return redirect('posts:lista')
        return super().dispatch(request, *args, **kwargs)    

    def form_valid(self, form):
        form.instance.slug = self.object.slug
        messages.success(self.request, "Post salvo com sucesso.")
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, View):
        
    def post(self, request, slug):
        
        post = get_object_or_404(Post, slug=slug)
        
        if post.autor != request.user:
            messages.error(request, 'Você não tem permissão para acessar ou editar este post.')
            return redirect('posts:lista')
        
        post.delete()
        messages.success(request, 'Post deletado com sucesso.')
        return redirect('posts:lista')
    
    def get(self, request, slug):
        
        post = get_object_or_404(Post, slug=slug)
        
        if post.autor != request.user:
            messages.error(request, 'Você não tem permissão para acessar ou editar este post.')
            return redirect('posts:lista')
        
        return render(
            request,
            'posts/confirmar_deletar_post.html',
            {'post':post}
        )
