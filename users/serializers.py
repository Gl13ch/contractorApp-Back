from rest_framework import serializers
from .models import User

from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password','phone')

    def create(self, validated_data):
        user = User.objects.create(
        email = validated_data['email'],
        password = make_password(validated_data['password']),
        phone = validated_data['phone']
        )
        user.save()
        return {"id": user.id, "email": user.email, "password": "", "phone": user.phone}

    def update(self, instance, validated_data):
        user = User.objects.get(id=instance.id)
        user.email = validated_data["email"]
        user.password = make_password(validated_data["password"],
        phone = validated_data['phone']
        )
        user.save()
        return user