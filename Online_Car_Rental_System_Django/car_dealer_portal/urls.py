from django.urls import path,include
from car_dealer_portal.views import *
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^index/$',include(index)),
    re_path(r'^login/$',include(login)),
    re_path(r'^auth/$',include(auth_view)),
    re_path(r'^logout/$',include(logout_view)),
    re_path(r'^register/$',include(register)),
    re_path(r'^registration/$',include(registration)),
    re_path(r'^add_vehicle/$',include(add_vehicle)),
    re_path(r'^manage_vehicles/$',include(manage_vehicles)),
    re_path(r'^order_list/$',include(order_list)),
    re_path(r'^complete/$',include(complete)),
    re_path(r'^history/$',include(history)),
    re_path(r'^delete/$',include(delete)),
]
