from django.db import models
from django.utils import timezone

class Test(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255,
        default='Some string')
    text = models.TextField(default='Some string')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()            
    def __str__(self):
        return self.title
# Create your models here.
