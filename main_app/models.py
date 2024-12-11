from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

# Create your models here.
class Reflection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    media = ArrayField(
        models.URLField(),
        blank=True, 
        null=True,
        default=list
    )
    date = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("reflection-detail", kwargs={"reflection_id": self.id})
    