from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe 

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
    list_display = ('name', 'view_link' )
    inlines = [
        QuestionInline,
    ]

    def view_link(self, obj):
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(
                obj.get_absolute_url(),
                "Go to Survey"
            )
        )

    view_link.allow_tags = True
    view_link.short_description = "Go to Survey"
        

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
    
    list_display = ('answer', 'question' )

admin.site.register(Answer, AnswerAdmin)



