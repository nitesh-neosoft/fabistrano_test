"""blongo_proj URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from blongo_app.views import index, update, delete, search, create

urlpatterns = [
    url(r'^$', index, name='post_index'),
    # url(r'^admin/', admin.site.urls),
    url(r'^create/', create, name="post_create"),
    url(r'^update/', update, name="post_update"),    
    url(r'^search/', search, name='post_search'),
    # url(r'^delete/', delete, name="post_delete"),
    url(r'^post_delete/(?P<pk>[a-z\d]+)', delete, name="post_delete"),
    # url(r'^post_delete/(?P<pk>[a-z\d]+)', DeletePostView.as_view(), name="post_delete"),
    
]
