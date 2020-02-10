
from django.db import models
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import BooleanField
from django.db.models import TextField
from django.db.models import EmailField

#from django.db.models import PasswordField

# Create your models here.
class Org(models.Model):
	org_name=models.CharField(max_length=20)
	email=models.EmailField()
	password=models.CharField(max_length=15)
	address=models.CharField(max_length=30)
	contact=models.IntegerField(10)
	total_amt=models.IntegerField()
	bank_acc= models.IntegerField()

	def __str__(request):
		return self.org_name
	

	def is_valid_organization(self):
		return(self.org_name == 'Nhhs')

class ChildEduDonor(models.Model):
	full_name=models.CharField(max_length=30)
	contact=models.IntegerField(10)
	address=models.CharField(max_length=50)
	street=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	postal_code=models.IntegerField(10)
	country=models.CharField(max_length=20)
	email=models.EmailField()
	donate_catagory=models.CharField(max_length=50)
	donate_amt=models.IntegerField()
	comments=models.CharField(max_length=300)
	org=models.ForeignKey(Org, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.full_name

class PoorDonor(models.Model):
	full_name=models.CharField(max_length=30)
	contact=models.IntegerField(10)
	address=models.CharField(max_length=50)
	street=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	postal_code=models.IntegerField(10)
	country=models.CharField(max_length=20)
	email=models.EmailField()
	donate_catagory=models.CharField(max_length=50)
	donate_amt=models.IntegerField()
	comments=models.CharField(max_length=300)

	def __str__(self):
		return self.full_name

class HomeDonor(models.Model):
	full_name=models.CharField(max_length=30)
	contact=models.IntegerField(10)
	address=models.CharField(max_length=50)
	street=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	postal_code=models.IntegerField(10)
	country=models.CharField(max_length=20)
	email=models.EmailField()
	donate_catagory=models.CharField(max_length=50)
	donate_amt=models.IntegerField()
	comments=models.CharField(max_length=300)

	def __str__(self):
		return self.full_name

class User(models.Model):
	first_name=models.CharField(max_length=10)
	last_name=models.CharField(max_length=10)
	username=models.CharField(max_length=15)
	email=models.EmailField()
	password=models.CharField(max_length=50)
	confirm_password=models.CharField(max_length=50)
	

	def __str__(self):
		return self.first_name

class Receiver(models.Model):
	full_name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	contact=models.IntegerField(10)
	email=models.EmailField()
	distribute_catagory=models.BooleanField(default=False)
	distribute_amt=models.IntegerField()
	receiver_acc=models.IntegerField()
	distribute_handcash=models.IntegerField()
	org=models.ForeignKey(Org, on_delete=models.CASCADE)

	def __str__(self):
		return self.full_name


class Upload(models.Model):
	Title=models.CharField(max_length=100)
	Date=models.DateField()
	image=models.ImageField(upload_to='images/')
	Description=models.CharField(max_length=3000)
	

	
	def __str__(self):
		return self.Title		

	


