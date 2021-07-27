from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def article_list(request):
    articles=Article.objects.all()

    return render(request,'articles/article_list.html',{'article':articles})

def article_detail(request,slug):
    print('helolooooooooooloolo')
    article=Article.objects.get(slug=slug)
    print(article)
    return render(request,'articles/article_details.html',{'articl':article})

@login_required(login_url='accounts:login')
def article_create(request):
    return render(request,'articles/article_create.html')