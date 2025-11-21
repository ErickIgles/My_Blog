from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CadastroUsuarioForm(UserCreationForm):    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placehold': 'Digite seu e-mail'
            }
        )
    )

    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placehold': 'Digite o seu nome de usuário'
            }
        )
    )
    
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placehold': 'Digite sua senha'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Confirme a sua senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placehold': 'Confirme a sua senha'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_existe = User.objects.filter(
            email=email
        )
        
        if email_existe.exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )
            
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_existe = User.objects.filter(
            username=username
        )
        
        if '@' in username:
            raise forms.ValidationError(
                'O nome de usuário não pode conter @.'
            )

        if username_existe.exists():
            raise forms.ValidationError(
                'Esté nome de usuário já está em uso.'
            )
        
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        password_confirm = cleaned_data.get('password2')

        if password and password_confirm:
            if password != password_confirm:
                self.add_error(
                    'password2',
                    'Senhas não são iguais.'
                )
        
        return self.cleaned_data


class UsuarioLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o seu nome de usuário'
            }
        )
    )
    
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )
