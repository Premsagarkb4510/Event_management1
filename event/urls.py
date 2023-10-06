"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about', views.about,name='about'),
    path('booking', views.booking, name='booking'),
    path('gallery', views.gallery, name='gallery'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),
    path('error', views.error, name='error'),
    path('login', views.Login1, name='login'),
    path('logout', views.Logout, name='logout'),
    path('yes/<y>',views.ad_approve, name='approve'),
    path('no/<n>',views.ad_reject, name='reject'),
    path('register', views.C_Register, name='customer_register'),
    path('e_register', views.E_Register, name='event_register'),
    # path('e_details', views.E_Details, name='event_data'),
    path('registered_events', views.ad_regevents, name='registered_events'),
    path('admin_verify', views.E_Verify, name='admin_verify'),



]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)