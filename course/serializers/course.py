from rest_framework import serializers

from course.models import BaseCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCourse
        fields = '__all__'
