from rest_framework import serializers

from user.models import Company


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'effective_username',
            'name',
            'email',
            'website',
            'creation_date',
            'about',
            'address',
            'telephone_number',
        ]


class CompanyProfileUpdateSerializer(CompanyProfileSerializer):
    class Meta:
        model = Company
        fields = CompanyProfileSerializer.Meta.fields
