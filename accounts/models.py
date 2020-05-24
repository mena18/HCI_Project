from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

worker_choices = {
('none','none'),
('painter','painter'),
('cleaner','cleaner'),
('plumber','plumber'),
}

class User(AbstractUser):
    is_engineer = models.BooleanField(default=False)
    is_foreman = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    type = models.CharField(max_length=10,choices=worker_choices,default='none')

    def __str__(self):
        if(self.is_engineer):
            return f"{self.username} : Engineer"
        if(self.is_foreman):
            return f"{self.username} : Foreman"
        else:
            return f"{self.username} : {self.type}"

    # for foreman
    def levels(self):
        lis=[]
        for level in self.level_set.all():
            lis.append(str(level.name))
        if(len(lis)>1):
            return f"Levels ({' , '.join(lis)})"
        else:
            return f"Level : {lis[0]}"
