from rest_framework import serializers
from .models import student,college

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class collegeserializer(serializers.ModelSerializer):
    class Meta:
        model = college
        fields = '__all__'