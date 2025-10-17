from rest_framework.views import APIView #This is the basic "pattern" or "toolbox" we use to create our own custom API view 🧰. It gives us the ability to run different functions based on the type of request (GET, POST, etc.).
from rest_framework.response import Response #This is a specialized tool used to return a response from an API. It automatically converts Python data (such as a dictionary or list) into a format the client understands (usually JSON).
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permission


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
    

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
       """Return a hello message"""
       a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
       return Response({'message':'Hello!','a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_methos':'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    #The most important feature of ModelViewSet is that it automatically provides all of the standard CRUD (Create, Read, Update, Delete) operations for you.
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #When the list operation is called, it returns the entire queryset. For operations that operate on a single object, such as retrieve, update, or destroy, it finds the correct object from the queryset using the ID (pk) from the URL. 
    authentication_classes = (TokenAuthentication,) #Tuple
    permission_classes = (permission.UpdateOwnProfile,)
       
       