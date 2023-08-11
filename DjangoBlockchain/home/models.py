from django.db import models

# Create your models here.
class CoinUser(models.Model):
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    amount = models.IntegerField(default=0, blank=True, null=True)
    privateKey = models.CharField(max_length=100)
    publicKey = models.CharField(max_length=100)

    def __str__(self):
        return self.username