from django.db import models


CATEGORY_CHOICES = (
    ('Website Development', 'Website Development'),
    ('Social Media Management', 'Social Media Management'),
    ('Website Traffic', 'Website Traffic Increase'),
)

class Product(models.Model):
    name = models.CharField(max_length=38, default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name