'''from django.db import models

# Create your models here.
class Madhu(models.Model):
    first_name=models.CharField(max_length=30)
    age=models.IntegerField()'''
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now() - datetime.timedelta(days=15)
        if now == self.pub_date:
            return True
        else:
            return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)