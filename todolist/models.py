from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    manage =models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

#This return the string name of the object in the database so that you can see it.
    def __str__(self):
        return self.task + " - " + str(self.done)