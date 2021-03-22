from django.urls import path
from .views import ListingsList
urlpatterns = [
	path("",ListingsList.as_view(),name="get_listings")
]
