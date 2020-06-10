from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
    ('Events', 'Events'),
    ('General Discussion', 'General Discussion')
)

class Post(models.Model):
    creator_id = models.ForeignKey(User, null=False, default=1)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.titles