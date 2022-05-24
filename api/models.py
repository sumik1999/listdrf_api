from email.policy import default
from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

class myModel(models.Model):

    text = models.CharField(max_length=255)
    data_list = ListCharField(
        base_field= models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11), 
    )
    data_object = models.JSONField(default=dict())