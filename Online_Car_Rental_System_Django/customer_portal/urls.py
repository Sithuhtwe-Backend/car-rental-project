from django.urls import path,include
from customer_portal.views import *
from django.urls import include, re_path
urlpatterns = [
    re_path(r'^index/$',include(index)),
    re_path(r'^login/$',include(login)),
    re_path(r'^auth/$',include(auth_view)),
    re_path(r'^logout/$',include(logout_view)),
    re_path(r'^register/$',include(register)),
    re_path(r'^registration/$',include(registration)),
    re_path(r'^search/$',include(search)),
    re_path(r'^search_results/$',include(search_results)),
    re_path(r'^rent/$',include(rent_vehicle)),
    re_path(r'^confirmed/',include(confirm)),
    re_path(r'^manage/',include(manage)),
    re_path(r'^update/',include(update_order)),
    re_path(r'^delete/',include(delete_order)),
]
