from django.db import models


# Create your models here.
class Tasks(models.Model):
    Title = models.CharField(max_length=150, blank=True, null=True)
    complated = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.Title)
