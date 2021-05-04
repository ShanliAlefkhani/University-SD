from django.db import transaction
from rest_framework import serializers

from user.models.person import Person
from user.serializers.user import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model = Person
        fields = ['user', 'username', 'password', 'name', 'surname', 'email', 'birthday', 'gender']

    def create(self, validated_data):
        with transaction.atomic():
            username = validated_data['user']['username']
            password = validated_data['user']['password']
            user = UserSerializer.create(UserSerializer(), validated_data={'username': username, 'password': password})
            person, created = Person.objects.update_or_create(user=user,
                                                              name=validated_data.get('name'),
                                                              surname=validated_data.get('surname'),
                                                              birthday=validated_data.get('birthday'),
                                                              gender=validated_data.get('gender'))
            return person
