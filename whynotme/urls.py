from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from .views import *
from . import views
#
router = routers.DefaultRouter()
# router.register(r'user/<int:pk>/posts/', )
router.register(r'users', UserViewSet)
# router.register(r'games', GameViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('edit-profile', UserViewSet.as_view({'get': 'list'}), name="edit-profile"),
    path('games/', GameViewSet.as_view(), name="create_game")
    # path('games/<int:user_id>/', GameViewSet.as_view({'get': 'list'}), name="games"),
    # path('api/', include(router.urls)),
]