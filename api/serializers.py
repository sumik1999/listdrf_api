from rest_framework import serializers
from .models import myModel


class myModelSerializer(serializers.ModelSerializer):
    
    text = serializers.CharField()
    data_list = serializers.ListField()
    data_object = serializers.JSONField()

    class Meta:
        model = myModel
        fields = ['text','data_list','data_object']

    