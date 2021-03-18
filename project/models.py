from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'cv/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    # generate urls for particular project details
    def get_absolute_url(self):
        return reverse('detail',kwargs={
            'project_id': self.id
        })
