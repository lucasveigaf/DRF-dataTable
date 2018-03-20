from django.conf import settings
from rest_framework import serializers

from risk.models import Risk
from risk.models import Responses


class RiskSerializer(serializers.ModelSerializer):
    last_modify_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Risk
        fields = ('id', 'title', 'parent', 'description', 'slug', 'last_modify_date', 'created')


class ResponsesSerializer(serializers.ModelSerializer):
    last_modify_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Responses
        fields = ('id', 'risk', 'responsesCategory', 'description', 'last_modify_date', 'created', 'deadlineDate')
