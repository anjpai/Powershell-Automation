from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=30)
    IPaddress=models.GenericIPAddressField()
    
    def __str__(self):
        return f"{self.id} {self.username} {self.IPaddress}"

# Create your models here.
