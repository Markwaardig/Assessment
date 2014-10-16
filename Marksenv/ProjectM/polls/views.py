from django.shortcuts import get_object_or_404, render

from polls.models import Question

# add discription ...  
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# add discription ...  
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

#    return HttpResponse("You're looking at question %s." % question_id)



# add discription ...  
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
# add discription ...  
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)