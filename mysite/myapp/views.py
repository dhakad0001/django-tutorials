from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_world(requests):
    html = '<h1>Hello World!</h1>'
    # we actually going to write some business logic here
    return HttpResponse(html)

def my_hotel_menu(requests):
    html = '''
        <ul>
            <li> Rasam </li>
            <li> Idli </li>
            <li> Dosa </li>
            <li> Sambhar </li>
        </ul>
    '''
    return HttpResponse(html)
