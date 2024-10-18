from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': "Main page of Property base",
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True
    }
    return render(request=request, template_name='main/index.html', context=context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')