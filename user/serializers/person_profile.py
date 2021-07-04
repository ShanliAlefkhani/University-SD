from rest_framework import serializers

from user.models import Person


class PersonProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['effective_username', 'name', 'surname', 'email', 'github_id', 'linkedin_id', 'birthday', 'gender']


class PersonProfileUpdateSerializer(PersonProfileSerializer):
    class Meta:
        model = Person
        fields = PersonProfileSerializer.Meta.fields
