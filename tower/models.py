from django.db import models
from accounts.models import User
# Create your models here.


class Report(models.Model):
    file = models.FileField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class Level(models.Model):
    foreman = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.IntegerField()
    reports = models.ManyToManyField(Report)


    def __str__(self):
        return f'LeveL({self.name})'

class Operation(models.Model):
    worker = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    progress = models.IntegerField()
    must_finish = models.IntegerField()
    deadline = models.DateField()
    finished = models.DateField()



class Messages(models.Model):
    level = models.ForeignKey(Operation,on_delete = models.CASCADE)
    progress_changing = models.IntegerField()
    content = models.TextField()
    sender = models.ForeignKey(User,related_name="sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name="receiver",on_delete=models.CASCADE)
