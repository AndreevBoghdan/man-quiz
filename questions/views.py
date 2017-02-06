from django.shortcuts import render
from .models import Question, Answer, Quiz

# Create your views here.

def questions(request, quiz_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    questions = []
    for question in Question.objects.filter(quiz=quiz):
        questions.append((question, question.answers.filter()))

    return render(request, 'questions/quiz.html',
        {'questions':questions}
        )
