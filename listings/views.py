from rest_framework import generics,viewsets,permissions
from .models import Listing
from .serializers import ListingSerializer,CreateListingSerializer


class ListingsList(generics.ListAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = ListingSerializer
	queryset = Listing.objects.all()


class ListingsEdit(generics.UpdateAPIView):
	pass


class ListingsDetail(generics.RetrieveDestroyAPIView):
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer


class ListingsCreate(generics.CreateAPIView):
	serializer_class = CreateListingSerializer
