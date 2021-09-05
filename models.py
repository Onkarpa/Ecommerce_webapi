from django.db import models

# Create your models here.
class Contact_Form(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    Mobile_no=models.CharField(max_length=50)
    email_id=models.EmailField()
    address=models.CharField(max_length=20)
    city_area=models.CharField(max_length=20)
    zip_no=models.IntegerField() 
    
    class Meta:
        db_table='Contact_Form'
    