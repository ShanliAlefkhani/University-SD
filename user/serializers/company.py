from django.db import transaction
from rest_framework import serializers

from user.models import Company
from user.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    user = UserSerializer(required=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ['token', 'user', 'username', 'password', 'name', 'creation_date', 'address', 'telephone_number']

    def create(self, validated_data):
        with transaction.atomic():
            username = validated_data['user.username']
            password = validated_data['user.password']
            user = UserSerializer.create(UserSerializer(), validated_data={'username': username, 'password': password})
            company, created = Company.objects.update_or_create(user=user,
                                                                name=validated_data.get('name'),
                                                                creation_date=validated_data.get('creation_date'),
                                                                address=validated_data.get('address'),
                                                                telephone_number=validated_data.get('telephone_number'))
            return company
