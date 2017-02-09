from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Survey(models.Model):
    class Meta():
        db_table = 'survey'

    name = models.CharField(max_length=200, default='new Survey')

    def get_absolute_url(self):
        return reverse('questions.views.questions', args=[str(self.pk)])

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

class Statistic(models.Model):
    class Meta():
        db_table = 'statistic'
    quiz_id = models.IntegerField(default=0)
    question_id = models.IntegerField(default=0)
    answer = models.CharField(max_length=200, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

@python_2_unicode_compatible
class Answer(models.Model):
    class Meta():
        db_table = 'answer'
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='answers')
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.answer

