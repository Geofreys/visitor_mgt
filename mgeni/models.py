from django.db import models

# Creating my models.
class Visitor(models.Model):
    name = models.CharField(max_length=30)
    ID_no = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    residence = models.CharField(max_length=20)
    reason = models.CharField(max_length=30)

