from rest_framework.views import APIView #This is the basic "pattern" or "toolbox" we use to create our own custom API view 🧰. It gives us the ability to run different functions based on the type of request (GET, POST, etc.).
from rest_framework.response import Response #This is a specialized tool used to return a response from an API. It automatically converts Python data (such as a dictionary or list) into a format the client understands (usually JSON).
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View""" #docstring
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        #request.data: This is the data (usually in JSON format) that the user sends via POST request. This is the ID of the person who wants to enter the door.

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    #It's like deleting all the old text in a Word document and pasting in completely new text. If you don't pass a field (for example, name) in the PUT request, that field is usually updated with a blank or default value.
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})
    #It's like editing just one sentence of a long text in a Word document. The rest of the text remains the same. This is a more efficient and widely preferred updating method.
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':"DELETE"})