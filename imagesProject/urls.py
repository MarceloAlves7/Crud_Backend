"""imagesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.http://127.0.0.1:8000/ function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from imagesApp.views import UsersViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from imagesApp import urls as imagesapp_urls




urlpatterns = [
    path('admin/', include(imagesapp_urls)),
    path('api/', include(imagesapp_urls))
     
    
]

#config imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#config React/
#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
