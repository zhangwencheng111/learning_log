"""learning_log URL Configuration

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
from learning_logs import views
from users import views as users_views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^topics/$', views.topics, name="topics"),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name="topic"),
    url(r'^new_topic/$', views.new_topic, name="new_topic"),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name="new_entry"),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name="edit_entry"),
    url(r'^users/login/$', login, {"template_name":"users/login.html"}, name="login"),
    url(r'^users/logout/$', users_views.login_view, name="logout"),
    url(r'^users/register/$', users_views.register, name="register"),
]
