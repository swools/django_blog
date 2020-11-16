from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):

    FAMILY = 'FAMILY'
    GARDEN = 'GARDEN'
    COOKING = 'COOKING'
    CATEGORIES = [
        (FAMILY, 'Family'),
        (GARDEN, 'Garden'),
        (COOKING, 'Cooking')
    ]
    category = models.CharField(max_length=25, choices=CATEGORIES, default='')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def get_color(self):
        color = ''
        if self.category == 'FAMILY':
            color = 'blue'
        elif self.category == 'GARDEN':
            color = 'green'
        elif self.category == 'COOKING':
            color = 'red'
        return color

    def when_posted(self):
        now = timezone.now()
        diff = now - self.created_on
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return f"{seconds} second ago"
            else:
                return f"{seconds} seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return f"{minutes} minute ago"
            else:
                return f"{minutes} minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return f"{hours} hour ago"

            else:
                return f"{hours} hours ago"
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return f"{days} day ago"

            else:
                return f"{days} days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return f"{months} month ago"

            else:
                return f"{months} months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return f"{years} year ago"

            else:
                return f"{years} years ago"
