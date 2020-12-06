'''为应用 users 定义 URL 模式'''

from django.conf.urls import url
from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views 

urlpatterns = [
    #登陆页面
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #注销页面
    url(r'^logout/$', views.logout_view, name='logout'),
    #注册页面
    url(r'^register/$', views.register, name='register'),
]
