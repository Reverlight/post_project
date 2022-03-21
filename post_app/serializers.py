from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers

from post_app.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Email address is required to log in'
            )

        if password is None:
            raise serializers.ValidationError(
                'Password is required'
            )
        print(email)
        print(password)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'There is no such user with specified email and password pair'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'User has been deactivated '
            )

        update_last_login(None, user)

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']
