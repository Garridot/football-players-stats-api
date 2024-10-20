from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny
from .serializers import *

class RegisterView(APIView):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self,request):
        serializer_class = UserSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()

        if serializer_class: 
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        return Response(serializer_class.data,status=status.HTTP_400_BAD_REQUEST)