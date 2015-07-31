from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'auction/login.html'}, name='login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auction/login.html'}, 
    	name='login_again'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/auction/'}, name='logout_page'),
    url(r'^bidding/$', views.bidding, name='bidding'),
]