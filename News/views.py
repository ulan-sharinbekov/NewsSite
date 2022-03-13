from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    xxx =  Category.objects.all()


    context = { 'news':news,
                'title':" Список новостей",
                'categories': categories,
                'xxx': xxx,
                }
    print(categories)
    return render(request, 'News/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    print(category)
    return render(request, 'News/category.html', {'news':news, 'categories':categories, 'category':category})
