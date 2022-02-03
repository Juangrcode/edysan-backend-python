"""Repairs URLs."""


# Django
from django.urls import path

# Views
from edysan.repairs.views import list_repairs, get_repair, create_repair, update_repair, delete_repair

urlpatterns = [
    path("repairs", list_repairs),
    path("repairs/<str:id>", get_repair),
    path("repairs/create", create_repair),
    path("repairs/update/<str:id>", update_repair),
    path("repairs/delete/<str:id>", delete_repair),
]
