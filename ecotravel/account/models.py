from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Destinations(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="product_images")
    Package_expense=models.IntegerField()


class Accomodation(models.Model):
    name=models.CharField(max_length=100)
    options=(
        ('Hotels','Hotels'),
        # ('Motels','Motels'),
        ('Guesthouse','Guesthouse'),
        ('Resort','Resort'),
        ('Treehouse','Treehouse')

    )
    Type=models.CharField(max_length=100,choices=options,default='Hotels')
    Rating=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="accomodation_images",null=True)
    img2=models.ImageField(upload_to="accomodation_images",null=True)

    def __str__(self):
        return self.name
    


class Selections(models.Model):
    accomodation=models.ForeignKey(Accomodation,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default="added")

class Orders(models.Model):
    accomodation=models.ForeignKey(Accomodation,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500)
    options=(
        ('Order Placed','Order Placed'),
        ('Cancelled','Cancelled')
       
    )
    order_status=models.CharField(max_length=100,default="order placed")

class Review(models.Model):
    review=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)
    accomodation=models.ForeignKey(Accomodation,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    


class BicycleModel(models.Model):
    yourname=models.CharField(max_length=100)
    youremail=models.EmailField()
    youraddress=models.CharField(max_length=500)
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    options=(
        ('Road Bike','Road Bike'),
        ('Mountain Bike','Mountain Bike'),
        ('Folding Bike','Folding Bike')
    )
    Type=models.CharField(max_length=100,choices=options,default='Road_bikes')




