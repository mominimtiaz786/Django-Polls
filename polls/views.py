from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
from django.http import HttpResponse

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list':latest_questions}
    return render(request,'polls/index.html',context)

def results(request,question_id):
    choice_set = Choice.objects.filter(question__id=question_id)
    response = '<br>'.join([c.choice_text+"     "+str(c.votes) for c in choice_set])
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})