from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
