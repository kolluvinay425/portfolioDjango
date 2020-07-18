from django.shortcuts import render
from .models import Project

# Create your views here.


def portfolio(request):

    context ={
        'my_url' : 'http://www.kkvinay.herokuapp.com'
    } 

    return render(request,'creations/portfolio.html',context)
