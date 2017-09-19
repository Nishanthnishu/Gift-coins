# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    pub_date = models.DateField('date published')
    cost = models.IntegerField(default=0)

class Answers(models.Model):
    question = models.ForeignKey(Questions)
    answer_text = models.CharField(max_length=500)
    pub_date = models.DateField('date published')
