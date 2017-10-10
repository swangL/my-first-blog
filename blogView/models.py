from django.db import models

# Create your models here.
# Models is basicly objects with attributes
# The models are saved in the database (here being sqlite3 - default)

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # search_tag = add a list of searchtag, so it's easier to find post

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
