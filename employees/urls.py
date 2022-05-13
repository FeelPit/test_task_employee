from django.conf.urls import url
from employees import views

urlpatterns = [
    url(r'^employee/$', views.employee_list),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.employee_detail),
    url(r'^city/$', views.city_list),
    url(r'^country/$', views.country_list),
    url(r'^country/(?P<pk>[0-9]+)/$', views.country_detail),
]