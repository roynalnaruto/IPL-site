from django.shortcuts import render
from auction.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'auction/home.html')

def login(request):
	return render(request, 'auction/login.html')

@csrf_protect
def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(
				username = cd['username'],
				first_name = cd['firstname'],
				last_name = cd['lastname'],
				password = cd['password1'],
				email = cd['email'])
			return HttpResponseRedirect('success/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('auction/register.html', variables)

def register_success(request):
	return render_to_response('auction/success.html')

@login_required
def bidding(request):
	return render_to_response('auction/bidding.html', {'user': request.user})