from django.db import models
from django.core.validators import RegexValidator

"""
A model that represents a person.

The `name` field is a CharField with a maximum length of 255 characters. The `name` field only accepts strings.
"""


class Person(models.Model):
    string_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message='Only string characters are allowed.'
    )
    name = models.CharField(max_length=255, validators=[string_validator], unique=True)

    class Meta:
        ordering = ['-name']
        db_table = 'person'

        def __str__(self) -> str:
            return self.name