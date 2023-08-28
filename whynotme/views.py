from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, filters
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

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    def post(self, request, format='json'):
        game_serializer = GameSerializer(data=request.data)
        
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_200_OK)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get_games(self):
    #     user_id = self.kwargs['user_id']
    #     queryset = GameViewSet.objects.filter(user_id=user_id)
    #     return queryset
# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class GameUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         exclude = ('user',)
# class UserLogViewSet(viewsets.ModelViewSet):
#     queryset = UserLog.objects.all()
#     serializer_class = UserLogSerializer

# class FilteredUserLogListView(generics.ListAPIView):
#     queryset = UserLog.objects.all()
#     serializer_class = UserLogSerializer

    # def get_queryset(self):
    #     user_id = self.kwargs['user_id']
    #     queryset = UserLog.objects.filter(user_id=user_id)
    #     return queryset

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = CustomUserSerializer

# def post(self, request, format='json'):
    #     user_serializer = UserSerializer(data=request.data)
        
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    #         return Response(user_serializer.data, status=status.HTTP_200_OK)
    #     return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get_users(self):
    #     user_id = self.kwargs['user_id']
    #     queryset = UserViewSet.objects.filter(user_id=user_id)
    #     return queryset