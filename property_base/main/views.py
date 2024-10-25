from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Main',
        'content': "Danang rental agency"
    }
    return render(request=request, template_name='main/index.html', context=context)

def about(request) -> HttpResponse:
    context = {
    'title': 'Home - About',
    'content': "About us",
    'text_on_page': "Welcome to our Da Nang real estate website! We are a team of professionals dedicated to helping you find the perfect property—whether residential or commercial—in one of the most scenic and rapidly growing cities in Vietnam: Da Nang. Our mission is to make the process of buying, selling, or renting property smooth, transparent, and stress-free for every client."
    }
    return render(request=request, template_name='main/about.html', context=context)