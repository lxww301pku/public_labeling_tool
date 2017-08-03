from django.db import models

class Sentence(models.Model):
    sent_text = models.CharField(max_length=200)
    domain = models.PositiveSmallIntegerField(default=0)
    intent = models.PositiveSmallIntegerField(default=0)
    slots = models.CharField(max_length=200)
    def __str__(self):
        return self.sent_text

