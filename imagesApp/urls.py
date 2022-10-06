from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ImageViewSet, UsersViewSet, ListImageUser, UploadImages, ListOneImageUser
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Users')
router.register('images', ImageViewSet, basename='Image')

routerImage = routers.DefaultRouter()
routerImage.register('oneimageuser', ListOneImageUser, basename='OneImage')


urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('users/<int:pk>/images/', ListImageUser.as_view()),
    path('users/<int:user_id>/images/uploadfiles/', UploadImages.as_view()),
    path('users/<int:user_id>/', include(routerImage.urls))
    
]

