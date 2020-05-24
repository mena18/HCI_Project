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
