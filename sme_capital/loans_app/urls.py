from django.conf.urls import url
from . import views
from .views import *


urlpatterns = [
	url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>[\d+])/$', views.profile, name='pk_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^create/$',  views.create_loan, name='create_loan'),    
]