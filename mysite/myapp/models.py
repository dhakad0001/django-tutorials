from django.db import models


class Student(models.Model):
    roll_no =  models.IntegerField()
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)

# class Course(models.Model):
#     pass 


# class Departments(models.Model):
#     pass