from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm
from django.http import HttpResponse
from .forms import CustomLoginForm, CustomUserCreationForm

# View to display the list of expenses
def index(request):
    expenses = Expense.objects.all().order_by('-created_at')
    return render(request, 'expenses/index.html', {'expenses': expenses})

# View to handle adding a new expense
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

# View to handle deleting an expense
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('index')
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change 'home' to your desired redirect URL
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})
def home_view(request):
    return HttpResponse("Welcome to Fintrackr!")

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

