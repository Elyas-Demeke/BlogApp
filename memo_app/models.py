from django.conf import settings
from django.db import models


class Note(models.Model):
    note_subject = models.CharField(max_length=15)
    note_body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_subject

