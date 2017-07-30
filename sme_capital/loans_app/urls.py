from django.conf.urls import url
from . import views
from .views import (
	profile,
	edit_profile,
	create_loan,
	loan_list,
	loan_detail,
	loan_edit,
	loan_delete,
)


urlpatterns = [
	url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>[\d+])/$', views.profile, name='pk_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^create/$',  views.create_loan, name='create_loan'), 
	url(r'^list/$', views.loan_list, name='list_loan'),   
	url(r'^(?P<slug>[\w-]+)/$', views.loan_detail, name='detail_loan'),   
	url(r'^(?P<slug>[\w-]+)/edit/$', views.loan_edit, name='edit_loan'),   
	url(r'^(?P<slug>[\w-]+)/delete/$', views.loan_delete, name='delete_loan'),   
]