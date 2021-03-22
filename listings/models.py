from django.db import models
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	icon = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Listing(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category,on_delete=models.PROTECT)
	price = models.IntegerField()
	description = models.CharField(max_length=300)
	published_time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name  # todo: change this print


class ListingImages(models.Model):
	image = models.ImageField(upload_to="")
	listing_id = models.ForeignKey(Listing,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.image)