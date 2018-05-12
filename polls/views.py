from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question , Choice
from django.http import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.

class IndexView(generic.ListView):
    
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailedView(generic.DetailView):
    template_name = 'polls/detail_que.html'
    model = Question

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist :
        raise Http404("Question does not Exist")
    template = 'polls/detail.html'
    context = {'question':question}
    return render(request,template,context)

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



