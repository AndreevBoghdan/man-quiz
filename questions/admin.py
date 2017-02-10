from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from models import Survey, Question, Answer, Statistic, Graphic
import signals

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
    list_display = ('name', 'view_link', 'statistics', 'graph' )
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


    def graph(self, obj):
        return mark_safe(
            '<a href="{0}">{1}</a>'.format(
                "/admin/questions/graphic/?survey__id__exact=" + str(obj.id),
                'Graph'
            )
        )

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
    fields=['answer', 'question' ]
    
    list_display = ('answer', 'question' )

admin.site.register(Answer, AnswerAdmin)

class UserCreateForm(UserCreationForm):
    
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.is_staff = True
        user.is_superuser=True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    add_form = UserCreateForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'email','password1', 'password2', ),
        }),
    )

    fieldsets = (
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'email')}),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class GraphicAdmin(admin.ModelAdmin):
    """
    Graphic admin
    """
    list_filter = ('survey',)
    search_fields = ['survey', ] 
    list_display = ('question_view', 'first_answer', 'second_answer', 'third_answer', 'fourth_answer', 'fifth_answer')
    fields=['question', ]
    readonly_fields=('question', 'survey' )


    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def question_view(self, obj):
        return obj.question

    def first_answer(self, obj):
        answers = Answer.objects.filter(question=obj.question)
        num_question = obj.question.number
        if int(num_question)!=0 and len(answers)>=1:
            num_answer = answers[0].number
            percent = round(float(num_answer) * 100 / int(num_question), 2)
            return str(answers[0]) + " - " + str(percent) + "%"
        else:
            return " "

    def second_answer(self, obj):
        answers = Answer.objects.filter(question=obj.question)
        num_question = obj.question.number
        if int(num_question)!=0 and len(answers)>=2:
            num_answer = answers[1].number
            percent = round(float(num_answer) * 100 / int(num_question), 2)
            return str(answers[1]) + " - " + str(percent) + "%"
        else:
            return " "

    def third_answer(self, obj):
        answers = Answer.objects.filter(question=obj.question)
        num_question = obj.question.number
        if int(num_question)!=0 and len(answers)>=3:
            num_answer = answers[2].number
            percent = round(float(num_answer) * 100 / int(num_question), 2)
            return str(answers[2]) + " - " + str(percent) + "%"
        else:
            return " "

    def fourth_answer(self, obj):
        answers = Answer.objects.filter(question=obj.question)
        num_question = obj.question.number
        if int(num_question)!=0 and len(answers)>=4:
            num_answer = answers[3].number
            percent = round(float(num_answer) * 100 / int(num_question), 2)
            return str(answers[3]) + " - " + str(percent) + "%"
        else:
            return " "

    def fifth_answer(self, obj):
        answers = Answer.objects.filter(question=obj.question)
        num_question = obj.question.number
        if int(num_question)!=0 and len(answers)>=5:
            num_answer = answers[4].number
            percent = round(float(num_answer) * 100 / int(num_question), 2)
            return str(answers[4]) + " - " + str(percent) + "%"
        else:
            return " "


admin.site.register(Graphic, GraphicAdmin)