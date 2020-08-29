from .models import Status, ServicePercentage
from rest_framework import serializers

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ('id', 'name')

class ServicePercentageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServicePercentage
		fields = ('percentage', )
	
