from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import CustomUser, Profile 

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ( 'email', 'username', 'password', 'first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
       
        fields = ('user', 'description', 'profile_picture','image_url')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_picture and request:
            return request.build_absolute_uri(obj.profile_picture.url)
        return None 
           

