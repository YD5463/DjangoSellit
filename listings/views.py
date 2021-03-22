from rest_framework import generics,viewsets,permissions
from .models import Listing
from .serializers import ListingSerializer


class ListingsList(generics.ListAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = ListingSerializer
	queryset = Listing.objects.all()


class ListingsEdit(generics.UpdateAPIView):
	pass


class ListingsDetail(generics.RetrieveAPIView):
	pass


class ListingsCreate(generics.CreateAPIView):
	pass
