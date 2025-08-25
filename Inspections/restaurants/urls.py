from django.urls import path, include
from . import views

app_name = 'restaurants' #this is where the request is made to

urlpatterns = [
    # name of url is gonna be "/chicago", YOU name it
    # to reference THIS path in html, you use restaurants:chi
    #   looks up the pattern named chi in the app name= restaurants

    #views.chicago goes to the chicago function.
    path('chicago/', views.chicago, name="chi"),

    # this is for the individual restaurant that was clicked
    path('chicago/<int:restaurant_id>/', views.chi_rest, name="chi_rest"),

    # this is for the chicago map
    path('chicago/map/', views.chi_map, name="chi_map"),

    path('restaurants-in-bounds/', views.restaurants_in_bounds, name='restaurants_in_bounds'),

]
