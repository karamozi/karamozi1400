from django.db import models
from django.contrib.auth.models import User


class Schools(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    school = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user) + ':' + self.school

class Classes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    capacity = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user) + ':' + self.school

class Table(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    num_of_session = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    first_day = models.CharField(max_length=200)
    first_start_time = models.CharField(max_length=200)
    first_end_time = models.CharField(max_length=200)
    second_day = models.CharField(max_length=200)
    second_start_time = models.CharField(max_length=200)
    second_end_time = models.CharField(max_length=200)
    signup_capacity = models.CharField(max_length=200)
    upload = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ':' + self.school
