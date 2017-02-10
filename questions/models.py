from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager


# Create your models here.

@python_2_unicode_compatible
class Survey(models.Model):
    class Meta():
        db_table = 'survey'
        verbose_name_plural = '   Survey'

    name = models.CharField(max_length=200, default='new Survey')

    def get_absolute_url(self):
        return reverse('questions.views.questions', args=[str(self.pk)])

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Question(models.Model):
    class Meta():
        db_table = 'question'
        verbose_name_plural = '  Question'
    question = models.TextField(max_length=200)
    count = models.IntegerField(default=0)
    survey = models.ForeignKey(Survey, related_name='questions', blank=True, null=True)
    number = models.IntegerField(default=0)


    def __str__(self):
        return self.question

class Statistic(models.Model):
    class Meta():
        db_table = 'statistic'
        verbose_name_plural = 'Statistic'
    quiz_id = models.IntegerField(default=0)
    question_id = models.IntegerField(default=0)
    answer = models.CharField(max_length=200, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

@python_2_unicode_compatible
class Answer(models.Model):
    class Meta():
        db_table = 'answer'
        verbose_name_plural = ' Answer'
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='answers')
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.answer

class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
