from rest_framework.routers import SimpleRouter 
from django.urls import path, include

from .views import BookViewSet, ChapterViewSet


router = SimpleRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'chapters', ChapterViewSet, basename='chapter')

urlpatterns = [
    path('api/v1/', include(router.urls))
]