from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length = 50)
    email = models.EmailField(max_length=25)
    subject = models.TextField()
    message= models.TextField()

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
