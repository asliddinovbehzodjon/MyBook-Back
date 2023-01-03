from django.db import models

# Create your models here.
class BotUsers(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    t_id = models.CharField(max_length=20,unique=True)
    language = models.CharField(max_length=5,default='en')
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name