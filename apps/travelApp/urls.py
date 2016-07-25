from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_travel_index'),
    url(r'^register/$', views.register, name = 'my_travel_register'),
]

