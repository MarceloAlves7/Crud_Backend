import email
from email.mime import image
from operator import ipow
import re
from rest_framework import viewsets, generics, status
from imagesApp.serializer import ImageSerializer, UserSerializer, ListImageUserSerializer
from imagesApp.models import Image, Usuario
from rest_framework.response import Response



class UsersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Users"""
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class ImageViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Users"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ListImageUser(generics.ListAPIView):
        """Exibindo todas as imagens de um User"""
        def get_queryset(self):
            queryset = Image.objects.filter(user_id=self.kwargs['pk'])
            return queryset

        serializer_class = ListImageUserSerializer



class UploadImages(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        user = kwargs['user_id']
        request.data['user']=user

        return self.create(request, *args, **kwargs)

class SignUser(generics.CreateAPIView):
    
    def post(self, request, *args, **kwargs):

        data = {
            'username': request.data.get('username'), 
            'full_name': request.data.get('full_name'), 
            'email': request.data.get('full_name'),
            'password': request.data.get('password')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









