from django.db import models
from django.contrib.auth.models import User


class Venu(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=60)
    phone = models.IntegerField('Phone', blank=True)
    web = models.URLField('website address')
    email_address = models.EmailField('email address')
    def __str__(self):
        return self.name
class MyclubUsers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('email address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    date = models.DateTimeField('event date and time')
    Venue = models.ForeignKey(Venu, blank=True, null=True, on_delete=models.CASCADE)
    #venu = models.CharField(max_length=120)
    #manager = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    attendees = models.ManyToManyField(MyclubUsers, blank=True)
    def __str__(self):
        return self.name


