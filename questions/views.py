from django.shortcuts import render
from .models import Question, Answer, Quiz

# Create your views here.

def questions(request, quiz_pk):
	quiz = Quiz.objects.get(pk=quiz_pk)
	return render(request, 'questions/quiz.html',
		{}
		)
