"""auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.all_auctions),
    url(r'^active$', views.active_auctions),
    url(r'^item/(?P<id>[0-9]+)$', views.item),
    url(r'^register$', views.register),
    url(r'^success/(?P<id>[0-9]+)$', views.success),
    url(r'^total$', views.results),
    url(r'^donations$', views.donations),
    url(r'^reset$', views.reset),
    url(r'^api/total$', views.api_result),
]
