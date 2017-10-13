"""SocialFollower URL Configuration

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

from Enter.views import RegisterUser
from Home.views import Home
from Order.views import FreeOrder, PremiumOrder


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home , name = 'home'),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^payment/',include('Payment.urls', namespace = 'payment' )),
    url(r'^enter/',RegisterUser, name="enter"),
    url(r'^freeorder/',FreeOrder.as_view(), name="freeorder"),
    url(r'^PremiumOrder/',PremiumOrder.as_view(), name="premiumorder"),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
