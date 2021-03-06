# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choices=models.ManyToManyField("Choice", related_name = "choices")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class QuestionForm(forms.Form):
    question_text = forms.CharField(label ='Question Text',max_length = 200)