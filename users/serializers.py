from rest_framework import serializers
from .models import User

from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password','phone','first_name', 'last_name', 'is_admin')

    def create(self, validated_data):
        user = User.objects.create(
        email = validated_data['email'],
        password = make_password(validated_data['password']),
        phone = validated_data['phone'],
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        is_admin = validated_data['is_admin']
        )
        user.save()
        return {"id": user.id, "email": user.email, "password": "", "phone": user.phone, "first_name": user.first_name, "last_name": user.last_name, "is_admin": user.is_admin}

    def update(self, instance, validated_data):
        user = User.objects.get(id=instance.id)
        user.email = validated_data["email"]
        user.password = make_password(validated_data["password"],
        phone = validated_data['phone'],
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        is_admin = validated_data['is_admin']
        )
        user.save()
        return user