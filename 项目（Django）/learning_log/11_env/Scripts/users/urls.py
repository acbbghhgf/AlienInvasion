'''为应用 users 定义 URL 模式'''

from django.conf.urls import url
from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views 

urlpatterns = [
    #主页
    #url(r'^$', views.index, name='index'),
    #登陆页面
    #path(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
