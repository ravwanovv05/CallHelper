from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        )