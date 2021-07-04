from rest_framework import serializers

from job.models import Job
from user.serializers import CompanySerializer


class JobSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ('company', 'title', 'image', 'requirements', 'field', 'salary', 'working_hours')

    def create(self, validated_data):
        job, created = Job.objects.update_or_create(company=self.context['request'].user.company,
                                                    title=validated_data.get('title'),
                                                    image=validated_data.get('image'),
                                                    expire_date=validated_data.get('requirements'),
                                                    field=validated_data.get('field'),
                                                    salary=validated_data.get('salary'),
                                                    working_hours=validated_data.get('working_hours'))
        return job

    def get_company(self, obj):
        company = CompanySerializer(obj.company).data
        company.pop('user')
        return company


class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'image', 'expire_date', 'field', 'salary', 'working_hours')
