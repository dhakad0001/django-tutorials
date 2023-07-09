from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 


class GetContextView(View):
    def get_context(self):
        return {
            'name': 'Prince Heer',

            'myhobbies': ['cricket', 'coding', 'chess', 'football'],
            
            'dict':{
                'key1': 'value1',
                'key2': 'value2'
            },

            'mylist': [
                '0 index',
                '1 index'
            ],

            'some_condition': True
        }

class HelloWorldView(GetContextView):
    def get(self, requests):
        context = self.get_context()
        return render(requests, 'myapp/hello_world.html', context)
    
class ShowPrinceHobbies(GetContextView):
    def get(self, requests):
        context = self.get_context()
        return render(requests, 'myapp/hobbies.html', context) 
    
    def post(self, requests):
        pass
    

# how we can render an html file in django
    # using the render method

def hello_world(requests):
    context = {
        'name': 'Prince Heer',

        'myhobbies': ['cricket', 'coding', 'chess', 'football'],
        
        'dict':{
            'key1': 'value1',
            'key2': 'value2'
        },

        'mylist': [
            '0 index',
            '1 index'
        ],

        'some_condition': True
    }

    return render(requests, 'myapp/hello_world.html', context)

# expressions -> a, b, a+b, a*b
# statements -> if statement, for loop, while loop, comprehension


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
