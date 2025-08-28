from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# FUNCION PARA registrar usuario 
class RegisterView(APIView):
    def post(self, request):                    
        username = request.data.get("username")
        password = request.data.get("password")
        if username and password:
            if User.objects.filter(username=username).exists():
                return Response({"error": "User already exits"}, status=status.HTTP_400_BAD_REQUEST)
            User.objects.create_user(username=username, password=password)
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)
    