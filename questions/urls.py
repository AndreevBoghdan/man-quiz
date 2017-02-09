from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^(?P<quiz_pk>\d+)/$', views.questions, name='questions'),
    url(r'^download/(?P<quiz_pk>\d+)/$', views.export_view, name='export_view'),
    url(r'^(?P<question_pk>\d+)/(?P<answer_pk>\d+)$', views.renew_number, name='renew_number'),
]
