from django.db import models

# Create your models here.
class Product_category(models.Model):
    PCid=models.IntegerField(primary_key=True)
    PCName=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.PCName
    
class Product(models.Model):
    PCName=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdescription=models.TextField()
    Pdate=models.DateField()

    def __str__(self) -> str:
        return self.Pname