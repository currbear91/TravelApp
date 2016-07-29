from django.shortcuts import render, redirect
from .models import User, UserManager, Place, Season, Activity, Season, Region, PlaceManager, SeasonPlace
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
		return redirect(reverse('my_travel_home'))
	else: 
		return redirect(reverse('my_travel_register'))

def processlogin(request):
	if request.method != "POST":
		return redirect(reverse('my_travel_index'))
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
	results3 = Place.placeManager.addReg()
	print("*"*10)
	print Region.objects.all()
	print("*"*10)
	reg = Region.objects.all()
	for x in reg:
		print x 
		print x.name
		print x.id
	print("*"*10)
	print request.POST['region']
	region = Region.objects.get(id= request.POST['region'])
	place = Place.objects.create(location = request.POST['location'], region = region, description = request.POST['description'])
	place2 = Place.objects.filter(location = request.POST['location'])

	places = Place.objects.all()

	test2 = request.POST['season']
	season = Season.objects.get(name = test2)
	place.season.add(season)


	test = request.POST.getlist('activity')
	for item in test:
		act = Activity.objects.get(name = item)
		place.activities.add(act)
		sp = SeasonPlace.objects.create(activity = act, season= season, place = place2[0], region = region )


	return redirect(reverse('my_admin_page'))

def delete(request, id):
	test = Place.objects.get(id = id)
	test.delete()
	return redirect(reverse('my_admin_page'))


def update(request, id):
	test = Place.objects.get(id = id)
	context = {
		'update': test,
	}
	return render(request, 'travelAppTemplates/update.html',context)
	

def updateprocess(request, id):
	update = Place.objects.get(id = id)
	update.region.name = request.POST['region']
	update.location.name = request.POST['location']
	update.season.name = request.POST['season']
	update.acitities.name = request.POST.getlist('activity')
	update.save()
	return redirect(reverse('my_admin_page'))

def travelprocess(request):
	bundle = []
	for item in Place.objects.all():
		arr = []
		arr2 = []
		arr.append(item.location)
		arr.append(item.description)
		arr.append(item.region.name)
		for x in item.season.all():
			arr.append(x.name)
		for y in item.activities.all():
			arr2.append(y.name)
			print("*"*5)
			print arr2
			print("*"*5)
		arr.append(arr2)
		print("*"*20)
		print arr
		print("*"*20)
		bundle.append(arr)
	print("*"*50)
	print bundle
	print("*"*50)

	print ("*"*30)
	print request.POST['season1']
	request.session['season1'] = request.POST['season1']
	request.session['activity1'] = request.POST['activity1']
	request.session['region1'] = request.POST['region1']
	request.session['bundle'] = bundle
	arr3 = []
	
	print len(bundle)
	for i in bundle:
		capture = False
		capture1 = False
		capture2 = False
		for j in i:
			print ("*"*5)
			print j
			print ("*"*5) 
			if j == request.session['region1']:
				capture = True
			if j == request.session['season1']:
				capture1 = True
				print 'success'
		for k in i[4]:
			if (k == request.session['activity1']):
				capture2 = True
				print k
		if capture == True and capture1 == True and capture2 == True:
			arr3.append(i)
		else:
			print 'fail'


	request.session['blue'] = arr3
	print ("*"*5)
			# if (bundle[jelly][2][ken] == request.session['activity1']) and (sea == request.session['season1']):
			# 	arr3.append(bundle[i])




	return redirect(reverse('my_travel_finder'))




def adminpage(request):
	context = {
		'seasons': Season.objects.all(),
		'place': Place.objects.all(),
		'activities': Activity.objects.all(),
		'seaspoon': SeasonPlace.objects.all(),
		'regions': Region.objects.all(),
	}
	return render(request, 'travelAppTemplates/admin.html', context)


def adminp(request):
	return render(request, 'travelAppTemplates/adminindex.html')

def home(request):
	context = {
		'seasons': Season.objects.all(),
		'activities': Activity.objects.all(),
		'regions': Region.objects.all(),
	}

	if 'id' not in request.session:
		return redirect(reverse('my_travel_index'))

	else:
		user = User.objects.get(id = request.session['id'])
	return render(request, 'travelAppTemplates/home.html',context)



	return render(request, 'travelAppTemplates/home.html',context)


def register(request):
	return render(request, 'travelAppTemplates/registration.html')

def userProfile(request):
	return render(request, 'travelAppTemplates/userProfile.html')

def specificTrip(request):
	context = {
		'places': Place.objects.all(),


	}
	return render(request, 'travelAppTemplates/specificTrip.html',context)

def finderResults(request):

	context = {
		'bundle': request.session['bundle'],
		'blue': request.session['blue'],

	}
	return render(request, 'travelAppTemplates/finderResults.html', context)

def destinationResults(request):
	return render(request, 'travelAppTemplates/destinationResults.html')

 
def logout(request):
	
	request.session.clear()
	return redirect(reverse('my_travel_index'))

