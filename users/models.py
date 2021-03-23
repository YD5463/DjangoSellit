from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as t


class CustomUserManager(BaseUserManager):
	def create_user(self,email,phone_number,password,username,**other):
		user = self.model(phone_number=phone_number,email=email,username=username,**other)
		user.set_password(password)  # create hash
		user.save()
		return user

	def create_superuser(self,email,phone_number,password,username,**other):
		other.setdefault('is_superuser', True)
		if other.get("is_superuser") is not True:
			raise ValueError("is superuser field must be set to True")
		return self.create_user(email,phone_number,password,**other)


class NewUser(AbstractUser):
	email = models.EmailField("email address",unique=True)
	phone_number = PhoneNumberField()
	gender = models.CharField(max_length=1, choices=(
		('M', 'Male'),
		('F', 'Female'),
		('D', 'Decline To Answer'),
	),default='D')
	about = models.TextField(t('about'), max_length=500, blank=True)
	last_login = models.DateTimeField(default=timezone.now)
	profile_image = models.ImageField(upload_to="media/profile_images")
	is_seller = models.BooleanField(default=False)
	username = models.CharField(max_length=100)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','phone_number']
