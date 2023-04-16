from django.shortcuts import loader, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import  Question, Choice
# Create your views here.


#on this it will show the latest questions abot 5 of them(if upto)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#Show specific questions and choices

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

#Show the question and the results selected


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

#Vote func

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #MAKE IT DISPLAY THE VOTING FORM AGAIN
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
    
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #returning HTTPResponseReditrects helps you minimize the risk of double posting
        return HttpResponseRedirect(reverse('polls:results', args = (question_id, )))    
