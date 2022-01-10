from django.db import models

class Contact(models.Model):
    name= models.CharField(max_length = 500)
    email = models.EmailField()
    subject = models.TextField()
    message= models.TextField()

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
