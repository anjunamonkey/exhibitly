from django.shortcuts import render
from core.models import *

def landing_page(request):
    """
    Landing page view
    """
    context = {
    }
    return render(request, 'core/landing.html', context)

def landing_page_kids(request):
    """
    Landing page for kids view
    """
    context = {
    }
    return render(request, 'core/landing-kids.html', context)

def landing_page_museums(request):
    """
    Landing page for museums view
    """
    context = {
    }
    return render(request, 'core/landing-museums.html', context)


def dashboard(request):
    """
    Dashboard view for museums
    """
    context = {
    }
    return render(request, 'app/dashboard.html', context)

def exhibition_detail(request):
    """
    Exhibition detail view
    """
    # exhibition = Exhibition.objects.get(id=exhibition_id)
    context = {
        # 'exhibition': exhibition,
    }
    return render(request, 'app/exhibition.html', context)

def museum_listing(request):
    """
    Museum listing view
    """
    context = {
    }
    return render(request, 'app/museum_listing.html', context)

def museum_detail(request):
    """
    Museum detail view
    """
    context = {
    }
    return render(request, 'app/museum_detail.html', context)