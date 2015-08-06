"""MB URL Configuration

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
from blogapp import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/create/', views.create_article),
    url(r'^article/showlist/', views.showlist_article),
    url(r'^article/modify/', views.modify_article),
    url(r'^article/view/', views.view_article),
    url(r'^article/detail/$', views.view_detail),
    url(r'^article/search/$', views.search_article),
    url(r'^article/tag/$', views.search_tags),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^comstatic/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    # url(r'^tinymce/',include('tinymce.urls')), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'media'}), 

] 
# + static(settings.STATIC_URL, document_root='./static/')


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
