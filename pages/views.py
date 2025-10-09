from django.shortcuts import render
from django.utils.translation import get_language
from .models import Hero, Post, Business, Feature, Product, CompanyProfile, History, Progress, Type

app_name = 'pages'

def index(request):
    current_language = get_language()
    heroes = Hero.objects.all()
    posts = Post.objects.all()
    businesses = Business.objects.all()
    features = Feature.objects.all()
    products = Product.objects.all()
    company_profile = CompanyProfile.objects.first()  # Use .first() if expecting a single profile
    history = History.objects.all()
    progresses = Progress.objects.all()
    types = Type.objects.all()

    context = {
        'current_language': current_language,
        'heroes': heroes,
        'posts': posts,
        'businesses': businesses,
        'features': features,
        'products': products,
        'company_profile': company_profile,
        'history': history,
        'progresses': progresses,
        'types': types,
    }
    return render(request, 'base.html', context)
