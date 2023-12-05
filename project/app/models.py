from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phno = models.CharField(max_length=15)
    age = models.IntegerField()
    from_destination = models.CharField(max_length=255)
    to_destination = models.CharField(max_length=255)
    airplane_no = models.CharField(max_length=10)
    seat_no = models.CharField(max_length=5)
