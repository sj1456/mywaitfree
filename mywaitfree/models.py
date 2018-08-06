from django.db import models

# Create your models here.
class Guest(models.Model):
    guest_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    register_time = models.DateTimeField('register time')

    def __str__(self):
        return self.guest_name
