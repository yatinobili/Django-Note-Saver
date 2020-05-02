from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=100, default='')
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return 'Entry {}'.format(self.id)

class Meta:
    verbose_name_plural = 'Entries'