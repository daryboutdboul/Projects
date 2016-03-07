from __future__ import unicode_literals

# Create your models here.

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Paris(models.Model):
    text=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.category+ ' :'+self.text
class Bet(models.Model):
    paris=models.ForeignKey(Paris,on_delete=models.CASCADE)
    bid=models.DecimalField(max_digits=4,decimal_places=2)
    bid_size=models.IntegerField()
    ask=models.DecimalField(max_digits=4,decimal_places=2)
    ask_size=models.IntegerField()
    login=models.CharField(max_length=10)
    def __str__(self):
        return str(self.bid)+ ' :'+str(self.ask)

class Trade(models.Model):
    paris=models.ForeignKey(Paris)
    level=models.DecimalField(max_digits=4,decimal_places=2)
    login_buyer=models.CharField(max_length=10)
    login_seller=models.CharField(max_length=10)

    