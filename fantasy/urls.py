from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from search import views as search_views
from contact import urls as contact_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls


urlpatterns = [
    # url(r'^django-admin/', include(admin.site.urls)),

    url(r'^shlinx/', include(wagtailadmin_urls)),
    url(r'^api/', include('api.urls')),
    url(r'^documents/', include(wagtaildocs_urls)),
]

urlpatterns += i18n_patterns(
    url(r'^listings/', include('listings.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^s/$', search_views.search, name='search'),
    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
