from rest_framework import serializers
from .models import User, Address

from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password','address','phone')

    def create(self, validated_data):
        user = User.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return {"id": user.id, "email": user.email, "password": ""}

    def update(self,instance, validated_data):
        user = User.objects.get(id=instance.id)
        user.email = validated_data["email"]
        user.password = make_password(validated_data["password"])
        user.save()
        return user

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','street_line1','street_line2','zip','city','state')