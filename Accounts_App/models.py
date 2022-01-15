from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)
        
class Product(models.Model):
    User = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=4 , decimal_places=2,null=True,blank=True)
    seler = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name