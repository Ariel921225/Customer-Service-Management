"""Ecommerce2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth.views import login, logout_then_login
from . import views

app_name='Customer'
urlpatterns = [
   url(r'^customer_view/(?P<pk>\d+)$', views.customer_view, name='customer_view'),
   url(r'^customer_edit/(?P<pk>\d+)$', views.customer_update, name='customer_edit'),
   url(r'^customer_delete/(?P<pk>\d+)$', views.customer_delete, name='customer_delete'),
   url(r'^customer_new$', views.customer_create, name='customer_new'),
   url(r'^index$', views.index, name='index')
   ]
