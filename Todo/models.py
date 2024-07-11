from django.db import models # type: ignore
from django.utils import timezone # type: ignore
# Create your models here.

class Todo(models.Model): 
    title = models.CharField(max_length=100)
    task = models.TextField(max_length=500, blank=False)
    dead_line = models.DateTimeField(default=timezone.now)

    def __dtr__(self): 

        return self.title
    
    