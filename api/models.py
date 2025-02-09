from django.db import models

# Create your models here.
class Bid(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    link = models.URLField()
    resume = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.position + ' - ' + self.company


