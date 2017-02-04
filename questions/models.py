from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Quiz(models.Model):
    class Meta():
        db_table = 'quiz'

    name = models.CharField(max_length=200, default='new Quiz')
    contentName = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name

class Question(models.Model):
    class Meta():
        db_table = 'question'
    question = models.TextField(max_length=200)
    count = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, related_name='quiz')


    def __str__(self):
        return self.question


class Answer(models.Model):
    class Meta():
        db_table = 'answer'
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='answers')
    is_Correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
