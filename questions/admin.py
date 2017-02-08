from django import forms
from django.contrib import admin
from models import Survey, Question, Answer

# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question

class AnswerInline(admin.TabularInline):
    model = Answer


class SurveyAdmin(admin.ModelAdmin):
    """
    Survey admin
    """
    inlines = [
        QuestionInline,
    ]

admin.site.register(Survey, SurveyAdmin)


class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin
    """
    fields=['question',]
    list_display = ( 'question', 'count')
    inlines = [
        AnswerInline,
    ]

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    """
    Answer admin
    """
    fields=['answer', 'is_Correct']
    
    list_display = ('answer', 'question', 'is_Correct')

admin.site.register(Answer, AnswerAdmin)



