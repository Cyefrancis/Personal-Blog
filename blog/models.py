from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField(max_length= 300)
    author = models.CharField(max_length= 50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
