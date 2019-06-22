from django.db import models

# Create your models here.


class Text(models.Model):

    story = models.CharField(max_length=10000)
    summary = models.CharField(max_length=10000)

    def __str__(self):
        return self.summary
