from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/users/',include("sellit.users.urls",namespace="users")),
    path('api/listings/',include(("listings.urls","listings"),namespace="listings")),
]
