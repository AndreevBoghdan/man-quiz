from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Answer, Question, Graphic


@receiver(post_save, sender=Question)
def default_answers(instance, created, **kwargs):
    if created:
        Answer.objects.create(answer='A', question=instance)
        Answer.objects.create(answer='B', question=instance)
        Graphic.objects.create(survey=instance.survey , question=instance)