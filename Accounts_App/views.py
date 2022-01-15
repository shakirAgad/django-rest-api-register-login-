''' this page to '''

from django.shortcuts import redirect
from rest_framework import generics , mixins, filters
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User,Product
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer,ProductSerializer


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler

    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    # post method
    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

# logout 
class Logout(generics.GenericAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)

        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

class Product(generics.ListAPIView):
    #model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['seler']
    ordering_fields = ['price']
    # def post(self, request, *args, **kwargs):
    #     serializer_class = ProductSerializer(data=request.data)
    #     if serializer_class.is_valid(raise_exception=True):
    #         return Response(serializer_class.data, status=HTTP_200_OK)

    #     return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
  

def index(request):
    return redirect('/api/login')
