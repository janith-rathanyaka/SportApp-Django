from django.db import models

# Create your models here.
class Sport(models.Model):
     author = models.CharField(max_length=30);
     title = models.CharField(max_length=30)
     description= models.TextField() 

     def _str_(self):
        return self.author