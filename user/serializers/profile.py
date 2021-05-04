from rest_framework import serializers

from user.models import Person


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'birthday', 'gender']


class ProfileUpdateSerializer(ProfileSerializer):
    class Meta:
        model = Person
        fields = ProfileSerializer.Meta.fields + ['username', 'password']
