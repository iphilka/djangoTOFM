from django.shortcuts import render
from .models import News
from datetime import datetime


# Create your views here.
def index(request):
    now = datetime.now()
    news = News.objects.all()
    news = news.order_by("-datetime")[0:3]
    return render(
        request,
        'index.html',
        {'news': news}
    )
