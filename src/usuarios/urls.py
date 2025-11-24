from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path(
        'cadastro/',
        views.CadastroUsuarioCreateView.as_view(),
        name='cadastro'
    ),
    path(
        'login/',
        views.UsuarioLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.UsuarioLogoutView.as_view(),
        name='logout'
    ),
    path(
        'me/',
        views.UsuarioPerfilDetailView.as_view(),
        name='perfil'
    ),
    path(
        'editar/',
        views.UsuarioUpdateView.as_view(),
        name='editar'
    ),
    path(
        'desativar/',
        views.UsuarioDesativarView.as_view(),
        name='desativar'
    ),
    path(
        'alterar_senha/',
        views.UsuarioPasswordUpdateView.as_view(),
        name='alterar_senha'
    ),
]