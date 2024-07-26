from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " ("+self.location+")"

class Designation(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name 


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    designation = models.ForeignKey(Designation , on_delete=models.CASCADE)
    dept = models.ForeignKey(Department , on_delete=models.CASCADE)
    date_of_joining = models.DateField(null=True)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=50 , default=0)
    salary = models.IntegerField(default=0)


    def __str__(self):
        return "%s %s " %(self.first_name, self.last_name ) 

class Attendance(models.Model):
    in_time = models.CharField(max_length=5, null=True, blank=True)
    out_time = models.CharField(max_length=5, null=True, blank=True)
    emp_date = models.DateField(default=date.today())
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default="P")

