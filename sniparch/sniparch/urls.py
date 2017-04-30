"""sniparch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from archive import views


urlpatterns = [
    url(r'^admin/',
        admin.site.urls),
    url(r'^index/',
        views.IndexPage.as_view(),
        name = 'index'),
    url(r'^query/list/$',
        views.QueryList.as_view(),
        name='list_query'),
    url(r'^query/create/$',
        views.QueryCreate.as_view(),
        name='create_query'),
    url(r'^tag/list/$',
        views.TagList.as_view(),
        name='list_tag'),
    url(r'^tag/create/$',
        views.TagCreate.as_view(),
        name='create_tag'),
    url(r'^snippet/list/$',
        views.SnippetList.as_view(),
        name='list_snippet'),
    url(r'^snippet/create/$',
        views.SnippetCreate.as_view(),
        name='create_snippet'),
    # url(r'^snippet/update/(?P<pk>[\w-]+)/$',
    #     views.SnippetUpdate.as_view(),
    #     name='update_snippet'),
    # url(r'^snippet/delete/(?P<pk>[\w-]+)/$',
    #     views.SnippetDelete.as_view(),
    #     name='delete_snippet'),
    # url(r'^snippet/detail/(?P<pk>[\w-]+)/$',
    #     views.SnippetDetail.as_view(),
    #     name='detail_snippet'),
]
