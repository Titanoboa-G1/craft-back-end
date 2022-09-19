from rest_framework import serializers
from .models import Event
from account.models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class userEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'start_time',
            'end_time',
        )

