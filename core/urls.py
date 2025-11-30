from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Root URL goes to landing page
    path('diners/', views.diners_page, name='diners_page'),  # Diners discount discovery page
    path('pricing/', views.pricing, name='pricing'),  # Pricing page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page

    path('app/menu/', views.menu_preview, name='menu_preview'),
    
    # Analytics Pages
    path('app/performance/', views.performance, name='performance'),
    path('app/heatmaps/', views.heatmaps, name='heatmaps'),
    path('app/insights/', views.insights, name='insights'),
    
    # Optimization Pages
    path('app/experiments/', views.experiments, name='experiments'),
    path('app/menu-optimizer/', views.menu_optimizer, name='menu_optimizer'),
    path('app/dynamic-pricing/', views.dynamic_pricing, name='dynamic_pricing'),
    path('app/promotions/', views.promotions, name='promotions'),
    
    # Configuration Pages
    path('app/menu-settings/', views.menu_settings, name='menu_settings'),
    path('app/integrations/', views.integrations, name='integrations'),
]
