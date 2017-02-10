from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe 

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from models import Survey, Question, Answer, Statistic

# Register your models here.

domain = 'http://h1475695.stratoserver.net'

class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 0
    fk_name = 'question'
    fields=['answer', ]


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 0
    fk_name = 'survey'
    fields=['question', ]
    inlines = [
        AnswerInline,
    ]


class SurveyAdmin(NestedModelAdmin):
    """
    Survey admin
    """
    list_display = ('name', 'view_link', 'statistics' )
    inlines = [
        QuestionInline, 
    ]

    def view_link(self, obj):
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(
                obj.get_absolute_url(),
                domain + obj.get_absolute_url()
            )
        )

    view_link.allow_tags = True
    view_link.short_description = "Go to Survey"

    def statistics(self, obj):
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(
                '/survey/download/' + str(obj.id),
                'Download statistics'
            )
        )

    view_link.allow_tags = True
    view_link.short_description = "Download statistics"

    def get_osm_info(self):
        # ...
        pass

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['osm_data'] = self.get_osm_info()
        return super(SurveyAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)
        

admin.site.register(Survey, SurveyAdmin)

"""class StatisticAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'datetime' )

admin.site.register(Statistic, StatisticAdmin)"""

class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin
    """
    list_filter = ('survey',)
    fields=['question','survey', ]
    list_display = ( 'question',)
    inlines = [
        AnswerInline,
    ]

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    """
    Answer admin
    """
    list_filter = ('answer',)
    fields=['answer', ]
    
    list_display = ('answer', 'question' )

admin.site.register(Answer, AnswerAdmin)



