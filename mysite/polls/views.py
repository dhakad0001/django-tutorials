from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question, Choice

def index(request):
    '''
    This view returns a list of all questions
    '''
    questions = Question.objects.all()
    
    context = {
        'question_list': [question for question in questions]
    }
    
    return render(request, 'polls/index.html', context)
    # return HttpResponse("Dummy response")

def detail(request, question_id):
    html = f"<h1>This page will show the<br> question no. {question_id}<br> with all its choices</h1>"
    return HttpResponse(html)

def results(request, question_id):
    html = f"<h1>This page will show polling result of question no. {question_id}</h1>"
    return HttpResponse(html)

def vote(request, question_id):
    html = f"<h1>You're voting for question no. {question_id}</h1>"
    return HttpResponse(html)