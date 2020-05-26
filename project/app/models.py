from django.db import models


# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=200, null=True)
	pan=models.CharField(max_length=20, unique=True,null=True)
	age=models.IntegerField(default=18)
	gender=models.CharField(max_length=200, null=True)
	email=models.EmailField(max_length=200, null=True, unique=True)
	city=models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

