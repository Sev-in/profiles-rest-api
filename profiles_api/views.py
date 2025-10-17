from rest_framework.views import APIView #This is the basic "pattern" or "toolbox" we use to create our own custom API view 🧰. It gives us the ability to run different functions based on the type of request (GET, POST, etc.).
from rest_framework.response import Response #This is a specialized tool used to return a response from an API. It automatically converts Python data (such as a dictionary or list) into a format the client understands (usually JSON).


class HelloApiView(APIView):
    """Test API View""" #docstring

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
