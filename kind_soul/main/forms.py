from django import forms
from .models import Comment

# для регистрации
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Базовые классы для форм регистрации и входа
from django.contrib.auth.models import User  # Модель пользователя


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Только поле контента для комментария
        
        
        
# Форма регистрации
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Введите ваш email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Форма входа
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)