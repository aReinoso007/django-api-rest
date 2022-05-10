from dataclasses import field
from rest_framework import serializers
from models import User

class User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id","name","contact","photo_url"]
