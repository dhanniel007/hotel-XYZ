from django.db import models

# Create your models here.

class Hotel_Record (models.Model):
    Room_Number = models.IntegerField()
    Amount_Paid = models.CharField(max_length=50)
    Occupant_Name =  models.CharField(max_length=6)
    Occupant_Email = models.EmailField(max_length=100)
    Occupant_Occupation = models.CharField(max_length=100)
    Number_Of_Nights =models.IntegerField()
    Start_Date = models.DateField()
    End_Date = models.DateField()
   


    def __str__(self):
        return self.First_name