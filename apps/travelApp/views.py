from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse

####################################################

# PROCESSING DATA 

####################################################

def processregister(request):
	results = User.userManager.isValidReg(request.POST)
	errors = results[1]
	for error in errors:
		messages.error(request, error)

	if results[0]:
		return redirect(reverse('my_travel_index'))
	else: 
		return redirect(reverse('my_travel_register'))

def processlogin(request):
	results = User.userManager.validlog(request.POST)
	print request.POST['username']
	if results[0]:
		print "************************************************"
		request.session['id'] = results[1].id
		print request.session['id']
		request.session['username'] = results[1].username
		print request.session['username']
		return redirect(reverse('my_travel_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.warning(request, error)
		return redirect(reverse('my_travel_index'))





####################################################

# DISPLAY PAGES SECTION  

####################################################

def index(request):
	return render(request, 'travelAppTemplates/index.html')

def adminform(request):
	return render(request, 'travelAppTemplates/admin.html')

def home(request):
	return render(request, 'travelAppTemplates/home.html')

def register(request):
	return render(request, 'travelAppTemplates/registration.html')

def userProfile(request):
	return render(request, 'travelAppTemplates/userProfile.html')

def specificTrip(request):
	return render(request, 'travelAppTemplates/specificTrip.html')

def finderResults(request):
	return render(request, 'travelAppTemplates/finderResults.html')

def destinationResults(request):
	return render(request, 'travelAppTemplates/destinationResults.html')

 
def logout(request):
	request.session.clear()
	return redirect(reverse('my_travel_index'))

