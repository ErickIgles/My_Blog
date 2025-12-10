from django.views.generic import ListView
from django.db.models import Q

from posts.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        qs = Post.publicados.all()\
            .select_related('autor')\
            .prefetch_related('tags')

        busca = self.request.GET.get('busca')
        
        if busca:
            qs = qs.filter(
                Q(titulo__icontains=busca) |
                Q(conteudo__icontains=busca)
            )

        return qs
     