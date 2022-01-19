from django.db import models

# Create your models here.

class NewUser(models.Model):

          username=models.CharField(max_length=30,primary_key=True)
          password=models.CharField(max_length=30)

          def __str__(self):
                    return self.username


class CheckNewUser(models.Model):

          
          password=models.CharField(max_length=30)
          username=models.CharField(max_length=30,primary_key=True)

          def __str__(self):
                    return self.username          
