from django.urls import path, include
from rest_framework import routers
from api.viewset.forum_viewset import ForumViewSet
from api.viewset.message_viewset import MessageViewSet
from api.viewset.topic_viewset import TopicViewSet





router = routers.DefaultRouter()
router.register(r'forum',ForumViewSet, basename='forum'),
router.register(r'messages',MessageViewSet, basename='messages'),
router.register(r'topic',TopicViewSet, basename='topic'),


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]

