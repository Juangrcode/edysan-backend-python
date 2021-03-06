"""Profile model."""

# Django
from django.db import models

# Urilities
from edysan.utils.models import EdysanModel


class Profile(EdysanModel):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True,
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=0,
        help_text="User's reputation based on the rides taken and offered.",
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
