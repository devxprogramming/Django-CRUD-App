from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=200, blank=False, null=False)
    lastname = models.CharField(max_length=200, blank=False, null=False)
    level = models.CharField(max_length=200, blank=False, null=False)
    # complete = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname