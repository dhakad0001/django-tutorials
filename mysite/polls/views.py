from django.shortcuts import render
from django.http import HttpResponse


from polls.models import Question, Choice


def show_polls(requests):
    q1 = Question.objects.get(id=1)
    q2 = Question.objects.get(id=2)

    context = {
        'q1': q1.question_text,
        'q2': q2.question_text
    }
    return render(requests, 'polls/index.html', context)


# how we can render an html file in django





