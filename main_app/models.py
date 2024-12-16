from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

class CarouselItem(models.Model):
    id == models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

REACTS = (
    ('L', 'Love'),
    ('H', 'Happy'),
    ('S', 'Sad'),
    ('C', 'Care')
)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("reflection-detail", kwargs={"reflection_id": self.id})
    

class Response(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    reaction = models.CharField(max_length=1, choices=REACTS, default=REACTS[0][0])
    reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Response by {self.user} on {self.created}: {self.comment[:30]}..."