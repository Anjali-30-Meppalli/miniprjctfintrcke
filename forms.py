from django import forms
from .models import Expense
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'description', 'amount']
        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'Category'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount'}),
        }
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
class CustomUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True)

class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Customize fields here