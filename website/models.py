from django.db import models
from django.core.exceptions import ValidationError

def custom_validate_email(value):
    if len(email)<8:
        raise ValidationError('Email is incorrect')

class Contact(models.Model):
    ip=models.GenericIPAddressField(null=True)
    name= models.CharField(max_length = 500)
    email = models.EmailField(max_length=254 , blank=False , validators=[custom_validate_email])
    subject = models.TextField()
    message= models.TextField()

    def __str__(self):
        return "Message from "+str(self.email)