from django.shortcuts import render
from core.models import *

def landing_page(request):
    """
    Landing page view
    """
    context = {
    }
    return render(request, 'core/abite.html', context)

def diners_page(request):
    """
    Diners page view - TooGoodToGo style discount discovery
    """
    context = {
    }
    return render(request, 'core/diners.html', context)

def pricing(request):
    return render(request, 'core/pricing.html')

def dashboard(request):
    """
    PostHog-style dashboard with A/B testing insights and AI chatbot
    """
    return render(request, 'app/dashboard.html')

# Analytics Pages
def performance(request):
    """Performance analytics with revenue trends and KPIs"""
    return render(request, 'app/performance.html')

def heatmaps(request):
    """Menu heatmap visualization showing click and engagement patterns"""
    return render(request, 'app/heatmaps.html')

def insights(request):
    """AI-driven insights and recommendations"""
    return render(request, 'app/insights.html')

# Optimization Pages
def experiments(request):
    """A/B testing dashboard for menu experiments"""
    return render(request, 'app/experiments.html')

def menu_optimizer(request):
    """AI menu layout optimizer with positioning recommendations"""
    return render(request, 'app/menu_optimizer.html')

def dynamic_pricing(request):
    """Dynamic pricing engine with demand-based adjustments"""
    return render(request, 'app/dynamic_pricing.html')

def promotions(request):
    """Automated promotion management with smart triggers"""
    return render(request, 'app/promotions.html')

# Configuration Pages
def menu_settings(request):
    """Menu item and category management"""
    return render(request, 'app/menu_settings.html')

def integrations(request):
    """POS and third-party service integrations"""
    return render(request, 'app/integrations.html')

