from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class EmployeeDetail(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100, null=True)
    schoolgpg = models.CharField(max_length=200, null=True)
    yearpassingpg = models.CharField(max_length=20, null=True)
    percentagepg = models.CharField(max_length=30, null=True)
    coursepggra = models.CharField(max_length=100, null=True)
    schoolgra = models.CharField(max_length=200, null=True)
    yearpassinggra = models.CharField(max_length=20, null=True)
    percentagegra = models.CharField(max_length=30, null=True)
    coursessc = models.CharField(max_length=100, null=True)
    schoolssc = models.CharField(max_length=200, null=True)
    yearpassingssc = models.CharField(max_length=20, null=True)
    percentagessc = models.CharField(max_length=30, null=True)
    coursehsc = models.CharField(max_length=100, null=True)
    schoolhsc = models.CharField(max_length=200, null=True)
    yearpassinghsc = models.CharField(max_length=20, null=True)
    percentagehsc = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100, null=True)
    company1desig = models.CharField(max_length=200, null=True)
    company1salary = models.CharField(max_length=20, null=True)
    company1duration = models.CharField(max_length=30, null=True)
    company2name = models.CharField(max_length=100, null=True)
    company2desig = models.CharField(max_length=200, null=True)
    company2salary = models.CharField(max_length=20, null=True)
    company2duration = models.CharField(max_length=30, null=True)
    company3name = models.CharField(max_length=100, null=True)
    company3desig = models.CharField(max_length=200, null=True)
    company3salary = models.CharField(max_length=20, null=True)
    company3duration = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class EmployeeSalary(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=30, null=True)
    position = models.CharField(max_length=100, null=True)
    joiningdate = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username
