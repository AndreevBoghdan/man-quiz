
import sqlite3
import os
import subprocess


from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Question, Answer, Survey, Statistic
import signals


#from pandas.io.sql import read_frame

# Create your views here.

@xframe_options_exempt
def questions(request, quiz_pk):
    survey = Survey.objects.get(pk=quiz_pk)
    questions = []
    for question in Question.objects.filter(survey=survey):
        questions.append((question, question.answers.filter()))

    return render(request, 'questions/quiz.html',
        {'questions':questions,
        'survey':survey}
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
            statistic = Statistic.objects.create(quiz_id=question.survey.id,question_id=question_pk, answer=answer.answer)
            return HttpResponse("OK")

def export_view(request, quiz_pk):
    """
    Export a csv file with data from database.
    """
    subprocess.call("rm output.csv", shell = True)
    con = sqlite3.connect(settings.DATABASE_NAME)
    df = read_frame("SELECT question_id, answer, datetime FROM statistic WHERE quiz_id = %s" % quiz_pk, con)
    df.to_csv(settings.OUTPUT_NAME, index=False, encoding='utf-8')
    f = open(settings.OUTPUT_NAME, 'r')
    response = HttpResponse(f, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=' + 'output.csv'
    return response
	