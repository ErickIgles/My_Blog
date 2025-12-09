from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from .models import Tag
from posts.models import Post

class TagListView(ListView):
    model = Tag
    template_name = 'tags/lista.html'
    context_object_name = 'tags'


class TagPostListView(ListView):
    model = Post
    template_name = 'tags/post_por_tag.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):    
        self.tag = Tag.objects.get(slug=self.kwargs['slug'])
        
        posts = Post.publicados.filter(tags=self.tag) \
            .select_related('autor') \
            .prefetch_related('tags')
        
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
