from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',  views.cms_page, name='cms_index'),  	   
]
