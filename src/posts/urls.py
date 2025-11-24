from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.PostListView.as_view(),
        name='lista'
    ),
    path(
        'formulario/',
        views.PostCreateView.as_view(),
        name='criar'
    ),
    path(
        '<slug:slug>/atualizar/',
        views.PostUpdateView.as_view(),
        name='atualizar'
    ),
    path(
        '<slug:slug>/deletar/',
        views.PostDeleteView.as_view(),
        name='deletar'
    ),
    path(
        '<slug:slug>/',
        views.PostDetailView.as_view(),
        name='detalhe'
    )    
]
