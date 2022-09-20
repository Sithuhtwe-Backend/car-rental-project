from home.views import *
from car_dealer_portal import *
from customer_portal import *
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^$',include(home_page)),
]
