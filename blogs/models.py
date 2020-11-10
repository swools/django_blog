from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Want to figure out how to calculate how old a post is and display in blog post card

    def get_date(self):
        """Get how many days, months, or years old a post is"""
        time = datetime.now()
        if self.created_on.day == time.day:
            return str(time.hour - self.date.hour) + " hours ago"
        else:
            if self.month == time.month:
                return str(time.day - self.date.day) + " days ago"
            else:
                if self.created_on.year == time.year:
                    return str(time.month - self.created_on.month) + " months ago"
        return self.created_on

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
