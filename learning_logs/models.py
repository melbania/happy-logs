from pagedown.widgets import PagedownWidget
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic)
    entry = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.entry) > 50:
            return self.entry[:50] + '...'
        else:
            return self.entry

    # def set_localtime(self):
    #     self.localtime = timezone.localtime(self.date_added)