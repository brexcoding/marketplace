from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Product(models.Model):
    image_link = models.CharField(max_length=555 ,unique=True, null=False,default=None)
    title = models.CharField(max_length=555 , null=True , default=None )
    price = models.CharField(max_length=555 , null=False,default=None)
    description = models.CharField(max_length=555 , null=False , default='')
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    min_order =  models.CharField(max_length=555 , null=True , default=None)
    product_id_field = models.AutoField(primary_key=True)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class  Order(models.Model):
    product = models.CharField(max_length=40 , null=False)
    name = models.CharField(max_length=40 , null=False)
    phone = models.CharField(max_length=10 , null=False)
    adress =  models.CharField(max_length=55 , null=False)
    adress1 = models.CharField(max_length=55 , null=False)
    amount = models.CharField(max_length=555 , null=False)
    def __str__(self) : 
        return self.name  