from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_travel_index'),
    url(r'^adminform/$', views.adminform, name = 'my_admin_form'),
    url(r'^adminpage/$', views.adminpage, name = 'my_admin_page'),
    url(r'^adminp/$', views.adminp, name = 'my_admin_p'),
    url(r'^register/$', views.register, name = 'my_travel_register'),
    url(r'^login/$', views.processlogin, name = 'my_travel_login'),
    url(r'^logout/$', views.logout, name = 'my_travel_logout'),
    url(r'^process/$', views.processregister, name = 'my_travel_process'),
    url(r'^home/$', views.home, name = 'my_travel_home'),
    url(r'^profile/$', views.userProfile, name = 'my_travel_profile'),
    url(r'^trip/$', views.specificTrip, name = 'my_travel_trip'),
    url(r'^finder/$', views.finderResults, name = 'my_travel_finder'),
    url(r'^destination/$', views.destinationResults, name = 'my_travel_destination'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'my_admin_delete'),
    url(r'^travelprocess$', views.travelprocess, name = 'my_travel_input'),
    url(r'^aupdate/(?P<id>\d+)$', views.update, name = 'my_admin_update'),
    url(r'^aupdatep/(?P<id>\d+)$', views.updateprocess, name = 'my_admin_updatep'),

]

