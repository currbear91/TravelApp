from django.shortcuts import render, redirect
from .models import User, UserManager, Place, Season, Activity
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
	
		request.session['id'] = results[1].id
		
		request.session['username'] = results[1].username

		request.session['first_name'] = results[1].first_name

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
	# try request.session['id']:
	# 	return redirect(reverse('my_travel_home'))
	# except KeyError:
	return render(request, 'travelAppTemplates/index.html')

def adminform(request):
	print("*"*10)
	fall = Season.objects.get(name = 'fall')
	print request.POST['location']
	print fall.name
	place = Place.objects.create(title = request.POST['location'])
	place.season.add(fall)
	spring = Season.objects.get(name = 'spring')
	place.season.add(spring)
	print spring.name
	summer = Season.objects.get(name = 'summer')
	place.season.add(summer)
	winter = Season.objects.get(name = 'winter')
	place.season.add(winter)
	print Place.objects.all()
	return redirect(reverse('my_admin_page'))

def adminpage(request):
	return render(request, 'travelAppTemplates/admin.html')


def adminp(request):
	return render(request, 'travelAppTemplates/adminindex.html')

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

