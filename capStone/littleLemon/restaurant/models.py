from django.db import models

# Create your models here.

class Booking(models.Model):
   Name = models.CharField(max_length=200)    
   #last_name = models.CharField(max_length=200)
   No_of_guests = models.IntegerField()
   BookingDate = models.DateTimeField()
   #comment = models.CharField(max_length=1000)

   #def __str__(self):
      #return self.first_name + ' ' + self.last_name

class Menu(models.Model):
   Title = models.CharField(max_length=255) 
   Price = models.DecimalField(max_digits=10, decimal_places=2)
   Inventory = models.IntegerField()
   
   def __str__(self):
      return self.Title