from django.db import models 



class Package(models.Model):
    senderName      = models.CharField(max_length=50)
    senderEmail     = models.EmailField(max_length=50)
    senderContact   = models.CharField(max_length=20)
    senderLocation  = models.CharField(max_length=20)
    trackingId      = models.CharField(max_length=15)

    # receivers details
    receiverName      = models.CharField(max_length=50)
    receiverEmail     = models.EmailField(max_length=50)
    receiverContact   = models.CharField(max_length=20)
    receiverLocation  = models.CharField(max_length=20)
    deliveryDate      = models.DateTimeField(auto_now=True)
    duedate           = models.DateField(blank=True, null=True)
    status            = models.CharField(max_length=20)
    country           = models.CharField(max_length=20)

    def __str__(self):
        return self.senderName


    
class CustomerRegister(models.Model):
    fullname        = models.CharField(max_length=100)
    country         = models.CharField(max_length=100)
    email           = models.EmailField(max_length=100)
    contact         = models.CharField(max_length=100)
    houseaddress    = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


