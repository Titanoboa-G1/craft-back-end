from dataclasses import field
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            "role",
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
            "description",
            "image",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if instance is not None:
            instance.set_password(password)
        instance.save()
        return instance