from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Survey(models.Model):
    class Meta():
        db_table = 'survey'

    name = models.CharField(max_length=200, default='new Survey')
    contentName = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Question(models.Model):
    class Meta():
        db_table = 'question'
    question = models.TextField(max_length=200)
    count = models.IntegerField(default=0)
    survey = models.ForeignKey(Survey, related_name='questions', blank=True, null=True)
    number = models.IntegerField(default=0)


    def __str__(self):
        return self.question

@python_2_unicode_compatible
class Answer(models.Model):
    class Meta():
        db_table = 'answer'
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='answers')
    is_Correct = models.BooleanField(default=False)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.answer

