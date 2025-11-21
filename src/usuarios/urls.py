from django.urls import path
from django.contrib.auth.views import LogoutView

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
    )
]