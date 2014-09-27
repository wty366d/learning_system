from django.conf.urls import patterns, include, url

from account import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/templates/account/login.html'},name='login'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html',},name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^password_change$', 'django.contrib.auth.views.password_change', {'template_name': 'account/password_change_form.html', 'post_change_redirect':'account:password_change_done' }, name='password_change'),
    url(r'^password_change_done$', 'django.contrib.auth.views.password_change_done', {'template_name': 'account/password_change_done.html'}, name='password_change_done'),
)
