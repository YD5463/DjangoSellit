from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
	def create_user(self,email,phone_number,name,password,**other):
		user = self.model(email=email,phone_number=phone_number,name=name,**other)
		user.set_password(password)  # create hash
		user.save()
		return user

	def create_superuser(self,email,phone_number,name,password,**other):
		other.setdefault('is_superuser', True)
		if other.get("is_superuser") is not True:
			raise ValueError("is superuser field must be set to True")
		return self.create_user(email,phone_number,name,password,**other)


class NewUser(AbstractUser):
	email = models.EmailField("email address",unique=True)
	phone_number = PhoneNumberField()
	gender = models.CharField(max_length=1, choices=(
		('M', 'Male'),
		('F', 'Female'),
	))
	last_login = models.DateTimeField(default=timezone.now)
	profile_image = models.ImageField(upload_to="media/profile_images")
	name = models.CharField(max_length=100)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name','phone_number']

