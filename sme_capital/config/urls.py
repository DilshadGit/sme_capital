from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from control_panal.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^loans/', include('loans_app.urls', namespace='loans_app')),
    url(r'^api/loans/', include('loans_app.loan_api.urls_api', namespace='loans_api')),
    url(r'^setting/', include('control_panal.urls', namespace='control_panal')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', home),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)