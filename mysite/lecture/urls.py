from django.conf.urls import patterns, include, url

from lecture import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    
    #url(r'^create/$', views.CreateView.as_view(), name='create'),
    
    
    url(r'^create/$', views.CreateFormView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', views.UpdateFormView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.DeleteFormView.as_view(), name='delete'),
)
