"""Repairs admin."""


# Django
from django.contrib import admin

# Model
from edysan.repairs.models.repairs import Repair, Comment


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    """Repair admin."""

    list_display = (
        "pk",
        "receiptNumber",
        "name",
        "lastName",
        "phone",
        "email",
        "status",
        "totalPrice",
        "deliveryDate",
    )
    search_fields = ("receiptNumber", "name")
    list_filter = ("status", "paymentCompleted")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin."""

    list_display = (
        "repair",
        "text",
    )
