from django.shortcuts import render, redirect
from .models import User, UserManager, Place, Season, Activity, Season, PlaceManager, SeasonPlace
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
	results = Place.placeManager.addSea()
	results2 = Place.placeManager.addAct()
	place = Place.objects.create(location = request.POST['location'])
	place2 = Place.objects.filter(location = request.POST['location'])
	# print test['season']
	test2 = request.POST['season']
	season = Season.objects.get(name = test2)
	place.season.add(season)
	test = request.POST.getlist('activity')


	print test
	for item in test:
		act = Activity.objects.get(name = item)
		place.activities.add(act)
		sp = SeasonPlace.objects.create(activity = act, season= season, place = place2[0])
		print act
		print SeasonPlace.objects.all()


	

	return redirect(reverse('my_admin_page'))

def delete(request, id):
	test = Place.objects.get(id = id)
	test.delete()
	return redirect(reverse('my_admin_page'))

def adminpage(request):
	context = {
		'seasons': Season.objects.all(),
		'place': Place.objects.all(),
		'activities': Activity.objects.all(),
		'seaspoon': SeasonPlace.objects.all()
	}
	return render(request, 'travelAppTemplates/admin.html', context)


def adminp(request):
	return render(request, 'travelAppTemplates/adminindex.html')

def home(request):
	context = {
		'seasons': Season.objects.all(),
		'activities': Activity.objects.all(),
	}

	return render(request, 'travelAppTemplates/home.html',context)

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

