from django.db import models

# Create your models here.


class Website(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    titleColor = models.CharField(max_length=500)
    textColor = models.CharField(max_length=500)
    style = models.TextField()
    url = models.URLField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
