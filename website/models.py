from django.db import models

class Contact(models.Model):
    ip=models.GenericIPAddressField(null=True)
    name= models.CharField(max_length = 500)
    email = models.EmailField(unique=True)
    subject = models.TextField()
    message= models.TextField()

    def __str__(self):
        return "Message from "+str(self.email)