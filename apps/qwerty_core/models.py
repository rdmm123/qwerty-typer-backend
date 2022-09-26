from random import randint

from django.db import models

# Create your models here.

class TextManager(models.Manager):
    def get_random_text(self, lang):
        q = self.all() if lang is None else self.filter(lang=lang)
        count = q.count()
        if count == 0:
            raise ValueError('No texts found')
        random = randint(0, count - 1)
        return q[random]

class Text(models.Model):
    text = models.CharField(max_length=500)
    lang = models.CharField(max_length=2)
    objects = TextManager()
    
    def __str__(self):
        return self.text
