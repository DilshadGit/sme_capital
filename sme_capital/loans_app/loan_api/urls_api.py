from django.conf.urls import include, url
from django.contrib import admin

from .view_api import (
	BusinessLoanCreateAPIView,
	BusinessLoanDetailAPIView,
	BusinessLoanDeleteAPIView,
	BusinessLoanEditAPIView,
	BusinessLoanListAPIView,
)

urlpatterns = [
    url(r'^$', BusinessLoanListAPIView.as_view(), name='list_api'),
    url(r'^(?P<slug>[\w-]+)/$', BusinessLoanCreateAPIView.as_view(), name='create_api'),
    url(r'^(?P<slug>[\w-]+)/$', BusinessLoanDetailAPIView.as_view(), name='detail_api'),
    url(r'^(?P<slug>[\w-]+)/edit/$', BusinessLoanEditAPIView.as_view(), name='edit_api'),
    url(r'^(?P<slug>[\w-]+)/delete/$', BusinessLoanDeleteAPIView.as_view(), name='delete_api'),
]
