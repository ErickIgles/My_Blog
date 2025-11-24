from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View

from .forms import CadastroUsuarioForm, UsuarioLoginForm, UsuarioUpdateForm, UsuarioPasswordChangeForm


class CadastroUsuarioCreateView(CreateView):
    template_name = 'usuarios/cadastro.html'
    model = User
    form_class = CadastroUsuarioForm
    success_url = reverse_lazy('usuarios:login')
    

class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'
    form_class = UsuarioLoginForm
    redirect_authenticated_user = True


class UsuarioLogoutView(LoginRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('usuarios:login')


class UsuarioPerfilDetailView(LoginRequiredMixin, DetailView):
    template_name = 'usuarios/perfil.html'
    model = User
    context_object_name = 'usuario'
    
    
    def get_object(self):
        return self.request.user


class UsuarioUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'usuarios/editar.html'
    model = User
    form_class = UsuarioUpdateForm
    success_url = reverse_lazy('usuarios:perfil')
    success_message = 'Dados atualizados com sucesso!'
    
    def get_object(self):
        return self.request.user


class UsuarioDesativarView(LoginRequiredMixin, View):
    
    def post(self, request):
        
        user = request.user
        user.is_active = False
        user.save()
        
        logout(request)
                
        messages.success(request, 'Conta desativada com sucesso.')
        return redirect('usuarios:login')


class UsuarioPasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/alterar_senha.html'
    form_class = UsuarioPasswordChangeForm
    success_url = reverse_lazy('usuarios:perfil')
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Senha atualizada com sucesso!')
        return super().form_valid(form)

