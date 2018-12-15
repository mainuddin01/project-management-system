from django.conf.urls import url

from . import views

app_name = 'projectmanager'

urlpatterns = [
    # url(r'^$', views.ProjectListView.as_view(), name='list'),
    url(r'^$', views.ProjectView.as_view(), name='myproject'),
    url(r'^create/$', views.ProjectCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/detail/$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.ProjectUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/detail/$', views.ModuleView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/modules/(?P<id>\d+)/$', views.TodoView.as_view(), name='modules'),
    url(r'^(?P<pk>\d+)/modules/(?P<id>\d+)/edit$', views.ModuleUpdateView.as_view(), name='module_edit'),
]
