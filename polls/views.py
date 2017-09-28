# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Question, Choice, QuestionForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        "Return last five published Questions"
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))

# My Views

def create_question(request):
    if request.method == 'POST':
        # put request data in form
        form = QuestionForm(request.POST)
        # check validity
        if form.is_valid():
            print('form is valid')
            question_text = form.cleaned_data['question_text']
            pub_date = timezone.now()
            q = Question(question_text= question_text,pub_date=pub_date)
            q.save()

            return HttpResponseRedirect(reverse('polls:detail', args=(q.pk,)))
    else:
        form = QuestionForm()

    return render(request, 'polls/create.html', {'form':form})



#def update(request)

#def delete(request)


#old code:
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context= {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question,
#     }
#     return render(request, 'polls/detail.html', context)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question,
#     }
#     return render(request, 'polls/results.html', context)