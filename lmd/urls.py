"""
URL configuration for lmd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from django.conf.urls.i18n import i18n_patterns
from authentication.views import home
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', home),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(path('admin/', admin.site.urls))
# urlpatterns.append(path('', admin.site.urls))

admin.site.site_header = 'M-TRANS'
admin.site.site_title = 'money transfert'
admin.site.index_title = 'm-trans'
