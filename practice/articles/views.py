from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def article_list(request):
    articles=Article.objects.all()

    return render(request,'articles/article_list.html',{'article':articles})

def article_detail(request,slug):
    return HttpResponse(slug)