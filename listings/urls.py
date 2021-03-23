from django.urls import path
from .views import ListingsList,ListingsEdit,ListingsDetail,ListingsCreate

urlpatterns = [
	path("",ListingsList.as_view(),name="get_listings"),
	path("<int:pk>/",ListingsDetail.as_view(),name="get_listing"),
	path("edit/",ListingsEdit.as_view(),name="edit_listing"),
	path("create",ListingsCreate.as_view(),name="create_listing"),
]
