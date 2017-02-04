from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^(?P<quiz_pk>\d+)/$', views.questions, name='questions'),
]
