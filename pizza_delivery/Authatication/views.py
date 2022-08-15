from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .serializer import UserSerializer
# Create your views here.

class HelloAuthAPIView(generics.GenericAPIView):
    def get(self,request):
        return Response({'message':'Auth successfully '},status=status.HTTP_200_OK)
    
    
class UserAPIView(generics.GenericAPIView):
    serializer_class=UserSerializer
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
