from .models import Status, ServicePercentage
from rest_framework import serializers

class StatusSerializer(models.Model):
	class Meta:
		model = Status
		fields = ('name')

class ServicePercentageSerializer(models.Model):
	class Meta:
		model = ServicePercentage
		fields = ('percentage')
	
