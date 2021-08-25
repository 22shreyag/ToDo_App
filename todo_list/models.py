from django.db import models
from django.db.models.expressions import F

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.item + ' | ' + str(self.completed)#this is used in admin page to dife data howit shoud be listed otherwise it will come in "List Object"