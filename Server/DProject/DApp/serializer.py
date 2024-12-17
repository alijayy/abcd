from rest_framework import serializer
from .models import Member

class memberSerializer(serializer.Serializer):
    class Meta:
        model = Member
        fields = '__all__'