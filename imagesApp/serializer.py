from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from imagesApp.models import Image, Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'full_name', 'email', 'password',]
    
    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



class ListImageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'