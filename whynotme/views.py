from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.db.models import Sum

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request, format='json'):
        custom_serializer = CustomUserSerializer(data=request.data)
        user_serializer = UserSerializer(data=request.data)
        
        if custom_serializer.is_valid():
            custom_serializer.save()
        else:
            return Response(custom_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if user_serializer.is_valid():
            user = user_serializer.save()
            if user:
                return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "unknown error"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer

class FilteredUserLogListView(generics.ListAPIView):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = UserLog.objects.filter(user_id=user_id)
        return queryset

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
