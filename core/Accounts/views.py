from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm

def register_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return HttpResponse("You have successfully signed up.")
    else:
        form = RegistrationForm()

    context = {'registration_form': form}
    return render(request, 'accounts/auth.html', context)



def logout_view(request):
	logout(request)
	return redirect('register')


def home(request):
    return render(request, 'home/home.html')