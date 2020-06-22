"""vip_number URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

# Header and Index of the site
admin.site.site_header = 'File Management'
admin.site.index_title = 'File Management'
admin.site.site_title = 'File Management'



handler404 = 'file_management.views.custom_page_not_found_view'
handler500 = 'file_management.views.custom_error_view'
handler403 = 'file_management.views.custom_permission_denied_view'
handler400 = 'file_management.views.custom_bad_request_view'

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    url(r'', include('file_management.users.urls')),
    # url(r'', include('file_management.pages.urls')),
    # url(r'', include('file_management.mydocuments.urls')),
    # url(r'', include('file_management.categories.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)