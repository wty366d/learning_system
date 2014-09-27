from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

#from mysite import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lecture/', include('lecture.urls',namespace='lecture')),
    url(r'^history/', include('history.urls',namespace='history')),
    url(r'^account/', include('account.urls',namespace='account')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', TemplateView.as_view(template_name="base.html"),name='index'),
    #url(r'^about/$',views.about()),
)





#if settings.DEBUG:
    #urlpatterns += patterns('',
        #url(r'^debuginfo/$', views.debug),
    #)
