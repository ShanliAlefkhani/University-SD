from django.db import transaction
from rest_framework import serializers

from user.models import Company
from user.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ['user', 'username', 'password', 'name', 'email', 'website',
                  'creation_date', 'about', 'address', 'telephone_number']

    def create(self, validated_data):
        with transaction.atomic():
            username = validated_data['user.username']
            password = validated_data['user.password']
            user = UserSerializer.create(UserSerializer(), validated_data={'username': username, 'password': password})
            company, created = Company.objects.update_or_create(user=user,
                                                                name=validated_data.get('name'),
                                                                email=validated_data.get('email'),
                                                                website=validated_data.get('website'),
                                                                creation_date=validated_data.get('creation_date'),
                                                                about=validated_data.get('about'),
                                                                address=validated_data.get('address'),
                                                                telephone_number=validated_data.get('telephone_number'))
            return company
