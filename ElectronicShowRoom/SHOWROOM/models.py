from django.db import models
import uuid 

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False) 
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}==={self.description}====={self.id}'

class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False) 
    name = models.CharField(max_length=255,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=1)
    brand = models.CharField(max_length=255,null=True,blank=True)
    image_url = models.ImageField(upload_to='images/',blank=True, null=True)
    count = models.IntegerField(default=0) 

    def __str__(self):
        return f'{self.name}==={self.category}==={self.price}==={self.brand}==={self.id}'
    
class Showroom(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False) 
    name = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    contact_info = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f'{self.name}==={self.location}==={self.contact_info}==={self.id}'

class Inventory(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, related_name='inventories')
    stock = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product}==={self.showroom}==={self.stock}==={self.id}'

class Order(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='order')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE,related_name='order')
    def __str__(self):
        return f'{self.product}==={self.quantity}==={self.total_price}==={self.showroom}==={self.id}'
