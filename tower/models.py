from django.db import models
from accounts.models import User
# Create your models here.

worker_choices = {
    ('none','none'),
    ('painting','painting'),
    ('testing pipes','testing'),
    ('fiting pipes','fitting'),
    ('clean rooms','rooms'),
    ('clean stairs','stairs'),
    ('clean bathrooms','bathrooms'),
}

worker_choices = {
('painter','painter'),
('cleaner','cleaner'),
('plumber','plumber'),
}

class Report(models.Model):
    file = models.FileField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class Level(models.Model):
    foreman = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.IntegerField()
    reports = models.ManyToManyField(Report,blank=True)


    def __str__(self):
        return f'LeveL({self.name})'


class Operation_type(models.Model):
    name = models.CharField(max_length=30)
    allowed = models.CharField(max_length=30,choices=worker_choices)

    def __str__(self):
        return f"{self.name} : {self.allowed}"

class Operation(models.Model):
    worker = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    type = models.ForeignKey(Operation_type,on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    must_finish = models.IntegerField()
    deadline = models.DateField()
    finished = models.DateField(blank=True,null=True)

    def __str__(self):
        return f'{self.type} : {self.progress}/{self.must_finish}'


class Messages(models.Model):
    level = models.ForeignKey(Operation,on_delete = models.CASCADE)
    progress_changing = models.IntegerField()
    content = models.TextField()
    sender = models.ForeignKey(User,related_name="sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name="receiver",on_delete=models.CASCADE)
