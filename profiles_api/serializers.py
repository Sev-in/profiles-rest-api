from rest_framework import serializers
#You can think of it like a security guard at the door of a club. 👮 He checks the identity (format) of the person trying to enter (incoming data) and lets them in if they comply with the rules.
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    #This serializer must expect a field named name.
    #The value of this field must be a CharField (i.e., text).
    #This text can be up to 10 characters long (max_length=10).

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    #ModelSerializer is a smart version that automatically understands your Django model (database table).

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only':True, #For security
                'style':{'input_type': 'password'} #***
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        # If the 'password' field is among the updated data
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)
    

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model= models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}