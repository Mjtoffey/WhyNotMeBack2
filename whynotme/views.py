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
        
        if custom_serializer.is_valid():
            custom_serializer.save()
            return Response(custom_serializer.data, status=status.HTTP_200_OK)
        return Response(custom_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer