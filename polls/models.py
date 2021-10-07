import datetime

from django.db import models
from django.forms import CharField
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text: models.CharField = models.CharField(max_length=200)
    pub_date: datetime.timedelta = models.DateTimeField('date published')

    def __str__(self) -> CharField:
        return self.question_text

    def was_published_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question: models.ForeignKey = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: models.CharField = models.CharField(max_length=200)
    votes: models.IntegerField = models.IntegerField(default=0)

    def __str__(self) -> CharField:
        return self.choice_text
