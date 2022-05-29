from enum import unique
from django.db import models
import uuid
from django_mysql.models import ListCharField


class myModel(models.Model):
    text = models.CharField(max_length=255)
    data_list = ListCharField(
        base_field= models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11), 
    )
    data_object = models.JSONField(default=dict())


class AcMaster(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state=models.CharField(max_length=400, null=False,blank=False , default="undefined")
    ac_no= models.IntegerField()
    ac_name= models.CharField(max_length=300, null=False,blank=False)
    pc_no= models.IntegerField()
    pc_name= models.CharField(max_length=300, null=False,blank=False)
    zone= models.CharField(max_length=300, null=False,blank=False)
    district_no= models.IntegerField()
    district_name= models.CharField(max_length=300)
    mp= models.CharField(max_length=300, null=False,blank=False)
    mla=models.CharField(max_length=300, null=False,blank=False)
    date_of_updation = models.DateField(auto_now=True)
    current_seat_category =models.CharField(max_length=20, null=False,blank=False)
    # unique_name = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
         return self.state+ " | " + str(self.ac_no) + " | " + str(self.id)

    # def save(self, *args, **kwargs):
    #     self.unique_name = str(self.state[:3]+self.district_name[:4]+self.ac_name[:3]+str(self.ac_no))
    #     super(AcMaster, self).save(*args, **kwargs)

    class Meta:
        ordering = ['ac_no']


class DemographyDetail(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ac= models.ForeignKey('AcMaster',on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=False,blank=False)
    type= models.CharField(max_length=200, null=False,blank=False)
    population=models.DecimalField(max_digits=10, decimal_places=3)
    date_of_updation = models.DateField(auto_now=True)

