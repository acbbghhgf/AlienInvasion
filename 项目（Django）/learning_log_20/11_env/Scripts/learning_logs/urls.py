'''定义 learning_logs 的 URL 模式'''

from django.conf.urls import url
from django.urls import path, re_path
from . import views 

urlpatterns = [
    #主页
    #re_path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('^topics/$', views.topics, name='topics'),
    path('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    path('^new_topic/$', views.new_topic, name='new_topic'),
    #用于添加新的条目的网页
    path('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    path('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
