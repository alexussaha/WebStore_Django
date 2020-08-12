"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "{0}, {1}".format(self.email, self.name)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"