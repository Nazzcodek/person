from django.db.models import fields
from rest_framework import serializers
from person_api.models import Person

"""
A serializer class for serializing and deserializing `Person` objects.

The `fields` property specifies the fields that should be included in the serialized output.
"""


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = "__all__"