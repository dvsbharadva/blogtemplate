from django.shortcuts import render, HttpResponse
from .models import Articles, CalltoAction
from django.views import generic

# Create your views here.
def welcome(request):
    articles = Articles.objects.all()
    call_to_action = CalltoAction.objects.get(id=1)
    published_article = articles.filter(status = 1)
    context = {
        'title': 'Home',
        'articles' : published_article,
        'calltoaction' : call_to_action
    }
    return render(request, "index.html", context)

def postDetail(request, slug):
    article = Articles.objects.get(slug='slug')
    call_to_action = CalltoAction.objects.get(id=1)
    context = {
        'artilce': article,
        'calltoaction' : call_to_action
    }
    return render(request, "post_detail.html", context)