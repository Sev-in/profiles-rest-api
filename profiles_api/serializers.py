from rest_framework import serializers
#You can think of it like a security guard at the door of a club. 👮 He checks the identity (format) of the person trying to enter (incoming data) and lets them in if they comply with the rules.

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    #This serializer must expect a field named name.
    #The value of this field must be a CharField (i.e., text).
    #This text can be up to 10 characters long (max_length=10).