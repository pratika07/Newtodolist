from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# defining a database table for posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # recording the timestamp when a new entry is created
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey defines a "many-to-one relationship"
    

    def __str__(self):
        return self.title

    # defining a URL for a new entry
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

