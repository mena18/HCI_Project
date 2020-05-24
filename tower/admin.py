from django.contrib import admin
from .models import Report,Level,Messages,Operation
# Register your models here.


admin.site.register(Report)
admin.site.register(Level)
admin.site.register(Operation)
admin.site.register(Messages)
