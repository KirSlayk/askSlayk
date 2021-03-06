from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from askSlaykApp.models import Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.


frequentlyAskedQuestion = []
for i in xrange(1,4):
	frequentlyAskedQuestion.append({
		'title' : 'How this: just do it? #{}'.format(i),
		'id' : i,
		'text' : 'This is very simple. Just do it.'
		})	


def base(request):
    return render(request,"base.html")


def registration(request):
    return render(request,"registrationform.html")


def login(request):
    return render(request,"loginform.html")


def ask(request):
    return render(request,"Ask_question.html")


def home(request):
	questions = Question.objects.all()
	paginator = Paginator(questions, 6)
	page = request.GET.get('page')
	try:
	    context = paginator.page(page)
	except PageNotAnInteger:
	    context = paginator.page(1)
	except EmptyPage:
	    context = paginator.page(paginator.num_pages)
	question_list = {'freqAsk' : frequentlyAskedQuestion, 'questions' : context}
	return render(request,"home.html", question_list)


@csrf_exempt
def post_get_params(request):
	output = ['Hello, my sweetest friend!<br>']
	
	output.append('Post test:')
	output.append('<form method="post">')
	output.append('<input type="text" name = "test">')
        output.append('<input type="submit" value="Submit">')
        output.append('</form>')

	if request.method == 'GET':
		if request.GET.urlencode() != '':
			output.append('Get data:')
			for key, value in request.GET.items():
				result=key+" = "+value
				output.append(result)
	if request.method == 'POST':
		output.append(request.POST.urlencode())
	return HttpResponse('<br>'.join(output))




def question(request, id = '1'):
	question = Question.objects.get(pk = id)	
	return render(request,"question.html", {'question' : question})


def index(request):

	#context = {'questions' : [json.dumps(q) for q in questions]}
	context_list = {'questions' : questions}
	context_list = tuple(context_list)
	paginator = Paginator(context_list, 6)
	page = request.GET.get('page')
	try:
	    context = paginator.page(page)
	except PageNotAnInteger:
	    context = paginator.page(1)
	except EmptyPage:
	    context = paginator.page(paginator.num_pages)
	return render (request, 'index.html', {"context" : context})

#def listing(request):
	

 

