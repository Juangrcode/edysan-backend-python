"""Repairs views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# Models
from edysan.repairs.models import Repair

# Serializer
from edysan.repairs.serializers import (
    RepairSerializer,
    CreateRepairSerializer,
    UpdateRepairSerializer,
    DeleteRepairSerializer,
)


@api_view(["GET"])
def list_repairs(request):
    """List repairs."""
    repairs = Repair.objects.all()
    serializer = RepairSerializer(repairs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_repair(request, id):
    """List one repair by id."""
    repair = Repair.objects.get(pk=id)
    serializer = RepairSerializer(repair)
    return Response(serializer.data)


@api_view(["POST"])
def create_repair(request):
    """Create repair."""
    print({"request": request})
    serializer = CreateRepairSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    repair = serializer.data
    print({"repair": repair})
    # repair = Repair.objects.create(**data)
    return Response(repair)
    name = request.data["name"]
    lastName = request.data["lastName"]
    email = request.data["email"]
    phone = request.data["phone"]
    repair = Repair.objects.create(name=name, lastName=lastName, email=email, phone=phone)
    data = {
        "name ": repair.name,
        "lastName ": repair.lastName,
        "email ": repair.email,
        "phone ": repair.phone,
    }

    return Response(data)


@api_view(["PUT"])
def update_repair(request, id):
    """Update repair by id,"""

    serializer = UpdateRepairSerializer(id, data=request.data)
    repair = Repair.objects.get(pk=id)
    print({"repair": repair})
    print({"serializer": serializer})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print({"serializer": serializer})
    # repair = Repair.objects.create(**data)
    return Response(repair)


@api_view(["DELETE"])
def delete_repair(request, id):
    """Delete repair by id,"""

    serializer = DeleteRepairSerializer(id)
    repair = Repair.objects.get(pk=id)
    print({"repair": repair})
    print({"serializer": serializer})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print({"serializer": serializer})
    # repair = Repair.objects.create(**data)
    return Response(repair)
