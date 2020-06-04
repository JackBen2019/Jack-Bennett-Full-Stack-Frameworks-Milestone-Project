from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('Website Development', 'Website Development'),
    ('Social Media Management', 'Social Media Management'),
    ('Website Traffic', 'Website Traffic Increase'),
)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    prod_creator_id = models.ForeignKey(User, null=False, default=1)
    name = models.CharField(max_length=38, default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name