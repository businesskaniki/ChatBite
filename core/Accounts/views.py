from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.views.decorators.cache import cache_control

def register_view(request, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			messages.success(request, "Registration successful." )
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'accounts/register.html', context)




def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")
	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = LoginForm()

	context['login_form'] = form
	return render(request,"accounts/login.html", context)




def logout_view(request):
	auth_logout(request)
	return redirect('login')
	




@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def home(request):
    context = {'user':request.user}
    return render(request, 'home/home.html',context)