from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_action(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_to = '/cars/'
            if request.GET.get('next'):
                redirect_to = request.GET.get('next')
            return redirect(redirect_to) # TODO: change to redirect to the url variable next
        else:
            form = AuthenticationForm()
        
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_action(request):
    logout(request)
    return redirect('cars_list')
