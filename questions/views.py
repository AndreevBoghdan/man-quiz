from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Question, Answer, Quiz


# Create your views here.

def questions(request, quiz_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    questions = []
    for question in Question.objects.filter(quiz=quiz):
        questions.append((question, question.answers.filter()))

    return render(request, 'questions/quiz.html',
        {'questions':questions,
        'quiz':quiz}
        )

def renew_number(request, question_pk, answer_pk):
    if request.method == "POST":
        if request.is_ajax():
            question = Question.objects.get(pk=question_pk)
            answer = Answer.objects.get(pk=answer_pk)
            question.number += 1
            answer.number += 1
            question.save()
            answer.save()
            return HttpResponse("OK")
	