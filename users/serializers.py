from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'phone_number', 'password']
        read_only = ['id']
        extra_kwargs = {
            'password': { 'write_only': True }
            }

    def create(self, validated_data): 
        user = User.objects.create_user(**validated_data)

        return user
