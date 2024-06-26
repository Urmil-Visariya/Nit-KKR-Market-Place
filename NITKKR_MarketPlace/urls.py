"""
URL configuration for NITKKR_MarketPlace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users import views as user_views
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from firstPage.views import *


urlpatterns = [
    path("main/", admin.site.urls),
    # path('',blog_views.home, name='home-page'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',user_views.logout_view,name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('admin/',admin_page),
    path('admin/add_product',add_product),
    path("",firstpage,name='home-page'),
    #path("firstpage/",firstpage),
    path("firstpage/<uuid>",prod_page),
    path("sell/",req_product),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)