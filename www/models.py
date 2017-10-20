# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Expense (models.Model):

    text = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):

        return '{} - {}'.format(self.text , self.date)

class Income (models.Model):

    user = models.ForeignKey(User)
    date = models.DateField()
    text = models.CharField(max_length=255)
    amount  = models.BigIntegerField()

    def __unicode__(self):

        return '{} - {}'.format(self.text , self.date)