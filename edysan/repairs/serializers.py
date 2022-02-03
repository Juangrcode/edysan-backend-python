"""Repair serializars."""


# Django REST Framework
from email import message
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

# Models
from edysan.repairs.models import Repair


class RepairSerializer(serializers.ModelSerializer):
    """Repair serializer."""

    # pk = serializers.CharField()
    # userId = serializers.CharField()
    # name = serializers.CharField()
    # lastName = serializers.CharField()
    # phone = serializers.CharField()
    # email = serializers.EmailField()
    # status = serializers.CharField()
    # lastStatus = serializers.CharField()
    # totalPrice = serializers.IntegerField()
    # paymentCompleted = serializers.BooleanField()
    # images = serializers.CharField()
    # description = serializers.CharField()
    # receiptNumber = serializers.IntegerField()
    # deliveryTime = serializers.CharField()
    # deliveryDate = serializers.DateField()

    class Meta:
        model = Repair
        fields = "__all__"

    def update(self, instance, data):
        print({"instance": instance, "self": self, "data": data})
        """Allow updates only before departure date."""
        return Repair.objects.update(**instance)


class CreateRepairSerializer(serializers.Serializer):
    """Create repair serializer."""

    user_id_regex = RegexValidator(
        regex=r"^[0-9a-fA-F]{24,24}$",
        message="Mongodb Id.",
    )
    userId = serializers.CharField(validators=[user_id_regex], max_length=24)
    name = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="Phone number ust be entered in the format: +999999999. Up to 15 digits allowed.",
    )
    phone = serializers.CharField(
        max_length=17,
        validators=[phone_regex, UniqueValidator(queryset=Repair.objects.all(), message="This number already exist")],
    )
    email_regex = RegexValidator(
        regex=r"[\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}$", message="Email validation with domain valid."
    )
    email = serializers.EmailField(
        validators=[
            email_regex,
            UniqueValidator(queryset=Repair.objects.all()),
        ]
    )
    status_regex = RegexValidator(
        regex=r"^(cancelled|pause|received|inProgress|sent|delivered)+$", message="This status is invalid."
    )
    status = serializers.CharField(
        required=False,
        max_length=12,
        validators=[status_regex],
    )
    lastStatus = serializers.CharField(
        required=False,
        max_length=12,
        validators=[status_regex],
    )
    totalPrice = serializers.IntegerField()
    paymentCompleted = serializers.BooleanField(required=False)
    images_regex = RegexValidator(
        regex=r"https?:\/\/[\w\-\\.]+:?[\w]+\.?\w{2,5}\/?\S*",
        message="Images url invalid.",
    )
    images = serializers.ListField(
        child=serializers.CharField(
            max_length=400,
            validators=[images_regex],
        )
    )
    description = serializers.CharField(required=False)
    receiptNumber = serializers.IntegerField()
    deliveryTime = serializers.CharField(max_length=50)
    deliveryDate = serializers.DateField()

    def create(self, data):
        print({"data": data})
        """Create circle."""
        return Repair.objects.create(**data)

    def update(self, instance, validated_data):
        # instance.userId = validated_data.get("userId", instance.userId)
        # instance.name = validated_data.get("name", instance.name)
        # instance.lastName = validated_data.get("lastName", instance.lastName)
        # instance.phone = validated_data.get("phone", instance.phone)
        # instance.email = validated_data.get("email", instance.email)
        # instance.status = validated_data.get("status", instance.status)
        # instance.lastStatus = validated_data.get("lastStatus", instance.lastStatus)
        # instance.totalPrice = validated_data.get("totalPrice", instance.totalPrice)
        # instance.paymentCompleted = validated_data.get("paymentCompleted", instance.paymentCompleted)
        # instance.images = validated_data.get("images", instance.images)
        # instance.description = validated_data.get("description", instance.description)
        # instance.receiptNumber = validated_data.get("receiptNumber", instance.receiptNumber)
        # instance.deliveryTime = validated_data.get("deliveryTime", instance.deliveryTime)
        # instance.deliveryDate = validated_data.get("deliveryDate", instance.deliveryDate)
        instance.save()
        return instance


class UpdateRepairSerializer(serializers.Serializer):
    """Update repair serializer."""

    user_id_regex = RegexValidator(
        regex=r"^[0-9a-fA-F]{24,24}$",
        message="Mongodb Id.",
    )
    userId = serializers.CharField(
        validators=[user_id_regex],
        max_length=24,
        required=False,
    )
    name = serializers.CharField(
        max_length=50,
        required=False,
    )
    lastName = serializers.CharField(
        max_length=50,
        required=False,
    )
    phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="Phone number ust be entered in the format: +999999999. Up to 15 digits allowed.",
    )
    phone = serializers.CharField(
        max_length=17,
        validators=[phone_regex, UniqueValidator(queryset=Repair.objects.all(), message="This number already exist")],
        required=False,
    )
    email_regex = RegexValidator(
        regex=r"[\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}$", message="Email validation with domain valid."
    )
    email = serializers.EmailField(
        validators=[
            email_regex,
            UniqueValidator(queryset=Repair.objects.all()),
        ],
        required=False,
    )
    status_regex = RegexValidator(
        regex=r"^(cancelled|pause|received|inProgress|sent|delivered)+$", message="This status is invalid."
    )
    status = serializers.CharField(
        required=False,
        max_length=12,
        validators=[status_regex],
    )
    lastStatus = serializers.CharField(
        required=False,
        max_length=12,
        validators=[status_regex],
    )
    totalPrice = serializers.IntegerField(
        required=False,
    )
    paymentCompleted = serializers.BooleanField(required=False)
    images_regex = RegexValidator(
        regex=r"https?:\/\/[\w\-\\.]+:?[\w]+\.?\w{2,5}\/?\S*",
        message="Images url invalid.",
    )
    images = serializers.ListField(
        child=serializers.CharField(
            max_length=400,
            validators=[images_regex],
            required=False,
        ),
        required=False,
    )
    description = serializers.CharField(required=False)
    receiptNumber = serializers.IntegerField(
        required=False,
    )
    deliveryTime = serializers.CharField(
        max_length=50,
        required=False,
    )
    deliveryDate = serializers.DateField(
        required=False,
    )

    def update(self, id, data):
        print({"id": id, "self": self, "data": data})
        """Allow updates only before departure date."""
        return Repair.objects.filter(pk=id).update(**data)


class DeleteRepairSerializer(serializers.Serializer):
    """Delete repair serializer."""

    def delete(self, id):
        return Repair.objects.filter(pk=id).delete()
