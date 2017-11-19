from django.contrib.auth import get_user_model
from rest_framework import serializers
from profiles.serializers import ProfileSerializer

# Get Django UserModel.
UserModel = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model with profile.
    """
    profile = ProfileSerializer()
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'profile')
        read_only_fields = ('email',)