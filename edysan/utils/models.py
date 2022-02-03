"""Django models utilities"""

# Django
from django.db import models


class EdysanModel(models.Model):
    """Edysan base model.

    EdysanModel acts as an abstracts base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + updated (DateTime): Store the last datetime the object was created.
    """

    updated = models.DateField(
        'updated at',
        auto_now=True,
        help_text='Date time on which the object was las modified.'
    )
    created = models.DateField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-updated']


# class Person(EdysanModel):
#     first_name = models.CharField()
#     last_name = models.CharField()

#     class Meta(EdysanModel.Meta):
#         db_table = 'student_role'


# class MyPerson(Person):
#     class Meta:
#         proxy = True

#     def say_hi(name):
#         print({'name': name})


# MyPerson.objects.all()
# juan = MyPerson.objects.get(on=1)
# juan.say_hi('Juan')

# rulo = Person.objects.get(ok=2)
# rulo.say_hi('Rulo')
