from django.db import models

# Create your models here.


class Contacts(models.Model):

    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    message = models.CharField(max_length=150)
    subject = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + self.email
    
#subscribeto nrewsletter
class emailsub(models.Model):
    email = models.EmailField()
   