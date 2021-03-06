"""fauxbible URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from godbrain import views

urlpatterns = [
    url(r'^get_random_quote/$', views.get_random_quote, name='get_random_quote'),
    url(r'^get_dirty_quote/$', views.get_dirty_quote, name='get_dirty_quote'),
    url(r'^dirty/', views.lets_get_dirty, name='lets_get_dirty'),
    url(r'^', views.lets_get_holy, name='lets_get_holy'),
    # url(r'^admin/', include(admin.site.urls)),
]
