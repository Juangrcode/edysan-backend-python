"""Repair Model."""

# Django
from django.core import validators
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator

# Utilities
from edysan.utils.models import EdysanModel


class Repair(EdysanModel):
    """Repair model.

    A repair is a group from repairs where be generate logs of users that want repairs his shoes. The admin can take log of any shoes with your respective type of repairs.
    """

    # Data user
    user_id_regex = RegexValidator(
        regex=r"^[0-9a-fA-F]{24,24}$",
        message="Mongodb Id.",
    )
    userId = models.CharField(validators=[user_id_regex], max_length=24)

    name = models.CharField("user name", max_length=50)
    lastName = models.CharField("last name", max_length=50)

    phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="Phone number ust be entered in the format: +999999999. Up to 15 digits allowed.",
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        # error_messages='This phone already exist.',
    )

    email_regex = RegexValidator(
        regex=r"[\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}$", message="Email validation with domain valid."
    )
    email = models.EmailField(
        validators=[email_regex],
        unique=True,
        # error_messages='This email already exist.',
        blank=True,
    )

    # Data repair
    status_regex = RegexValidator(
        regex=r"^(cancelled|pause|received|inProgress|sent|delivered)+$", message="This status is invalid."
    )
    status = models.CharField(validators=[status_regex], max_length=12, default="received")
    lastStatus = models.CharField(validators=[status_regex], max_length=12, null=True)

    totalPrice = models.FloatField(default=0)
    paymentCompleted = models.BooleanField(default=False)

    images_regex = RegexValidator(
        regex=r"https?:\/\/[\w\-\\.]+:?[\w]+\.?\w{2,5}\/?\S*", message="Images validate with url valid."
    )
    images = models.CharField(validators=[images_regex], max_length=400, null=True)

    description = models.TextField(blank=True)

    receiptNumber = models.PositiveIntegerField()

    deliveryTime = models.CharField(max_length=50, null=True)
    deliveryDate = models.DateField()

    def __str__(self):
        """Return user's str receipt number."""
        return str(self.receiptNumber)

    class Meta:
        """Metas class."""

        ordering = ["-receiptNumber", "-created"]


class Comment(models.Model):
    """Comment model."""

    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(max_length=300)

    def __str__(self):
        """Return user's str text of comment."""
        return self.text
