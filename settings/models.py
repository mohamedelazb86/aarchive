from django.db import models

class Document_Type(models.Model):
    code=models.CharField(max_length=75)
    name=models.CharField(max_length=120)
    notes=models.TextField(max_length=1500)

    def __str__(self):
        return self.name

class Sector(models.Model):
    code=models.CharField(max_length=75)
    name=models.CharField(max_length=120)
    notes=models.TextField(max_length=1500)

    def __str__(self):
        return self.name
