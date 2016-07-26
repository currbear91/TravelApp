from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_travel_index'),
    url(r'^adminform/$', views.adminform, name = 'my_admin_form'),
    url(r'^register/$', views.register, name = 'my_travel_register'),
    url(r'^home/$', views.home, name = 'my_travel_home'),
    url(r'^profile/$', views.userProfile, name = 'my_travel_profile'),
    url(r'^trip/$', views.specificTrip, name = 'my_travel_trip'),
    url(r'^finder/$', views.finderResults, name = 'my_travel_finder'),
    url(r'^destination/$', views.destinationResults, name = 'my_travel_destination'),
]

