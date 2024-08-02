from django.db import models
from django.db import models

class Emp(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    dept = models.CharField(max_length=50)

    def __str__(self):
        return self.name
