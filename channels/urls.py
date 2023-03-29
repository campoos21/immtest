from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from channels.views import ContentViewSet, ChannelViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter

# urlpatterns = [
#     path('content/', views.ContentList.as_view()),
#     path('channels/', views.ChannelList.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

router = SimpleRouter()
router.register(r'content', ContentViewSet)
router.register(r'channels', ChannelViewSet)
urlpatterns = router.urls

