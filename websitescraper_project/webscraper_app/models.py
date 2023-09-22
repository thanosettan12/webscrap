from django.db import models


# Create your models here.
class Links(models.Model):
    def __str__(self):
        return self.string_name
    address = models.CharField(max_length=1000, null=True, blank=True)
    string_name = models.CharField(max_length=250, null=True, blank=True)
