from django.db import models

# Create your models here.
class event_team_reg(models.Model):
    Team_name=models.CharField(max_length=30)
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=10)
    Address=models.CharField(max_length=20)
    Contact=models.IntegerField()
    License= models.TextField()
    Email=models.TextField()
    package = models.CharField(max_length=20)
    image = models.ImageField()
    logo = models.ImageField()
    status=models.CharField(max_length=20)


    def __str__(self):
        return self.Team_name

class customer_register(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    Username=models.CharField(max_length=25)
    Password=models.CharField(max_length=10)
    Confirm_Password = models.CharField(max_length=10,null=True)
    Email=models.EmailField()


    def __str__(self):
       return self.Username

class Login(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=10)
    St=models.CharField(max_length=1)


    def __str__(self):
        return self.Username




