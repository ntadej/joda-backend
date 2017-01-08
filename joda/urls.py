"""
Joda Backend URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from joda.helpers import JodaRouter, about_view
from joda_core.views.files import get_file_view

router = JodaRouter(trailing_slash=False)
router.add_features()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls + [url(r'about', about_view)])),
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^get/([0-9]+)', get_file_view)
]
