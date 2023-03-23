from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from .models import UserProfile

def register_view(request, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			print("this the form is valid**************************************************")
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			print("this the form is not valid+++++++++++++++++++++++++++++++++++++++++++++++++++++")
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'accounts/register.html', context)

def login_view(request):
	return render(request,"accounts/login.html")

def logout_view(request):
	logout(request)
	return redirect('register')


def home(request):
    return render(request, 'home/home.html')