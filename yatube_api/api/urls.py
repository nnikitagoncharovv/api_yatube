from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet


router_ver1 = DefaultRouter()
router_ver1.register('posts', PostViewSet, basename='posts')
router_ver1.register('groups', GroupViewSet, basename='groups')
router_ver1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_ver1.urls))
]
