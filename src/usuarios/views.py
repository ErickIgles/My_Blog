from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView

from .forms import CadastroUsuarioForm, UsuarioLoginForm


class CadastroUsuarioCreateView(CreateView):
    
    template_name = 'usuarios/cadastro.html'
    model = User
    form_class = CadastroUsuarioForm
    success_url = reverse_lazy('usuarios:login')
    

class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'
    form_class = UsuarioLoginForm
    redirect_authenticated_user = True

