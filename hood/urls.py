from django.conf.urls import url
from . import views

urlpatterns=[
  url('^$',views.area,name = 'area'),
  url('^home/(\d+)',views.home,name = 'home'),
  url('^profile',views.profile,name = 'profile'),

]