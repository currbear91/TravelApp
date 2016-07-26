from django.shortcuts import render, redirect
# from .models import User
from django.contrib  import messages
import datetime
# from ..examApp.models import TravelManager, UTravel, OTravel
from django.core.urlresolvers import reverse
def register(request):
	# if User.userManager.isValidReg(request.POST,request):
	# 	passflag = True
	# 	return redirect(reverse('my_travel_index'))

	# else:
	# 	passflag = False
		# return redirect(reverse('my_travel_index'))

	return render(request, 'travelAppTemplates/home.html')

def login(request):
	if User.userManager.login(request.POST, request):
		passflag=True
		return redirect(reverse('my_travel_home'))
	else: 
		passflag = False
		return redirect(reverse('my_travel_index'))

def process(request):

	pass

####################################################

# DISPLAY PAGES SECTION  

####################################################

def index(request):
	return render(request, 'travelAppTemplates/index.html')

def adminform(request):
	return render(request, 'travelAppTemplates/admin.html')

def home(request):
	return render(request, 'travelAppTemplates/home.html')

def userProfile(request):
	return render(request, 'travelAppTemplates/userProfile.html')

def specificTrip(request):
	return render(request, 'travelAppTemplates/specificTrip.html')

def finderResults(request):
	return render(request, 'travelAppTemplates/finderResults.html')

def destinationResults(request):
	return render(request, 'travelAppTemplates/destinationResults.html')
 

