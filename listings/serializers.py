from rest_framework import serializers
from .models import Listing,ListingImages


class ListingImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = ListingImages
		fields = ('image',)


class ListingSerializer(serializers.ModelSerializer):
	images = ListingImagesSerializer(many=True)

	class Meta:
		model = Listing
		fields = ("name","category","price","description","published_time",'images')

	def create(self, validated_data):
		images_data = validated_data.pop('images')
		listing = Listing.objects.create(**validated_data)
		for image in images_data:
			ListingImages.objects.create(listingid=image, **image)
		return listing

