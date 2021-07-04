from rest_framework import serializers

from job.models import Application
from job.serializers import JobSerializer
from user.serializers import PersonSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('job',)


class ApplicationListSerializer(serializers.ModelSerializer):
    job = serializers.SerializerMethodField(read_only=True)
    person = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Application
        fields = ('job', 'person')

    def get_person(self, obj):
        person = PersonSerializer(obj.person).data
        person.pop('user')
        return person

    def get_job(self, obj):
        job = JobSerializer(obj.job).data
        job.pop('company')
        return job
