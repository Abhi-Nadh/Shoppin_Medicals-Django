import datetime
from django.db import models

class MedicineData(models.Model):
    medicine_name=models.CharField(max_length=100)
    company=models.CharField(max_length=100,default='Cipla')
    price=models.FloatField()
    medicine_description=models.CharField(max_length=300)
    medicine_add_date=models.DateField(default=datetime.date.today())    