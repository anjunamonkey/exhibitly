from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Root URL goes to landing page
    path('kids/', views.landing_page_kids, name='landing_page_kids'),  # Kids landing page
    path('museums/', views.landing_page_museums, name='landing_page_museums'),  # Museums landing page
    path('app/', views.dashboard, name='dashboard'),  # Dashboard for museums
    path('app/exhibition/', views.exhibition_detail, name='exhibition_detail'),  # Exhibition detail page
    path('app/museums/', views.museum_listing, name='museum_listing'),  # Museum listing page
    path('app/museum/1/', views.museum_detail, name='museum_detail'),  # Museum detail page

]
