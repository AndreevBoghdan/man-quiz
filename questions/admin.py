from django import forms
from django.contrib import admin
from models import Quiz, Question, Answer

# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question

class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdmin(admin.ModelAdmin):
    """
    Quiz admin
    """
    inlines = [
        QuestionInline,
    ]

admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin
    """
    fields=['question', 'quiz']
    list_display = ( 'question', 'count')
    inlines = [
        AnswerInline,
    ]

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    """
    Answer admin
    """
    fields=['question', 'answer', 'is_Correct']
    
    list_display = ('answer', 'question', 'is_Correct')

admin.site.register(Answer, AnswerAdmin)



