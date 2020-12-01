'''定义 learning_logs 的 URL 模式'''

from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    #主页
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path(r'^topics/$', views.topics, name='topics'),
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    path(r'^new_topic/$', views.new_topic, name='new_topic'),
    #用于添加新的条目的网页
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]