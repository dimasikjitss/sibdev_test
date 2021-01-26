from rest_framework import serializers
from .models import CsvFile
from django.core.management.base import BaseCommand, CommandError


class CsvSerializer(serializers.ModelSerializer):

    class Meta:

        model = CsvFile
        fields = ('csv',)


class ProcessedFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CsvFile
        fields = ('username', 'spent_money', 'gems')