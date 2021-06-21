from rest_framework import serializers

from user.models import Person


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['effective_username', 'name', 'surname', 'email', 'github_id', 'linkedin_id', 'birthday', 'gender']


class ProfileUpdateSerializer(ProfileSerializer):
    class Meta:
        model = Person
        fields = ProfileSerializer.Meta.fields
