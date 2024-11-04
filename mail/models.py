from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Mail(models.Model):
    statment=models.CharField(max_length=120)
    document_type=models.CharField(max_length=120)
    date=models.DateField(default=timezone.now)
    notes=models.TextField(max_length=1500)
    file=models.FileField(upload_to='files_mail')

    def __str__(self):
        return self.statment
    

class User_Document(models.Model):
    statment=models.CharField(max_length=120)
    document_type=models.CharField(max_length=120)
    date=models.DateField(default=timezone.now)
    notes=models.TextField(max_length=1500)
    file=models.FileField(upload_to='files_user')
    user=models.ForeignKey(User,related_name='user_document',on_delete=models.CASCADE)

    def __str__(self):
        return self.statment

    
    
