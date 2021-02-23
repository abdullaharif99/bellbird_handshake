from django.db import models

# Create your models here.
class Chirp(models.Model):
    text = models.CharField(max_length=140)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.text