"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Paris(models.Model):
    text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.pub_date+ ' :'+self.text
class Bet(models.Model):
    paris=models.ForeignKey(Paris)
    bid=models.DecimalField(max_digits=4,decimal_places=2)
    bid_size=models.IntegerField()
    ask=models.DecimalField(max_digits=2,decimal_places=2)
    ask_size=models.IntegerField()
    login=models.CharField(max_length=10)
class Trade(models.Model):
    paris=models.ForeignKey(Paris)
    level=models.DecimalField(max_digits=2,decimal_places=2)
    login_buyer=models.CharField(max_length=10)
    login_seller=models.CharField(max_length=10)

    