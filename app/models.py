from django.db import models

# Create your models here.
class fee(models.Model):
    Name=models.CharField(max_length=25,blank=False,null=False)
    Bank_name=models.CharField(max_length=25,blank=False,null=False)
    
    
    def __str__(self) :
        return self.name