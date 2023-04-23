from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts-ver1')
router.register('groups', GroupViewSet, basename='groups-ver1')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments-ver1')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls))
]
