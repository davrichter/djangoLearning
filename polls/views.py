from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.

class IndexView(generic.ListView):
    template_name: str = 'polls/index.html'
    context_object_name: str = 'latest_question_list'

    def get_queryset(self) -> list[Question]:
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # I havent found the correct type for this
    model = Question
    template_name: str = 'polls/detail.html'


class ResultsView(generic.DetailView):
    # I havent found the correct type for this
    model: Question = Question
    template_name: str = 'polls/results.html'


def vote(request, question_id):
    question: Question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice: Choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context: dict[str, str] = {
            'question': question,
            'error_message': "You didn't select a choice",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
