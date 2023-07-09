from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requests):
    return render(requests, 'polls/index.html')


# how we can render an html file in django





