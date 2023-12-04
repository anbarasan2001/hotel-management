from django.db import models
class customer_modelTable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    mbl=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    class Meta:
        db_table='customer_registration'
class addroom_modelTable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    no_of_beds=models.CharField(max_length=50)
    status=models.CharField(default='available',max_length=50,null=True)
    class Meta:
        db_table='addrooms'
class booking_modelTable(models.Model):
    bid=models.AutoField(primary_key=True)
    rid=models.CharField(max_length=50)
    uid=models.CharField(max_length=50)
    status=models.CharField(default='booking',max_length=50)
    class Meta:
        db_table='booking'




