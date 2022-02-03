"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.http.response import HttpResponse

# Views
# from orders import views as orders_views


# import ipdb
# ipdb.set_trace()

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include(("edysan.repairs.urls", "repairs"), namespace="repair")),
]
