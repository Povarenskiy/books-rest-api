from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action


from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer

from .tasks import inc_chapter_field


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BookViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Представление Книги
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination


class ChapterViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Представление главы
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


    def retrieve(self, request, pk=None):
        update_field = 'views'
        inc_chapter_field.delay(pk, update_field)
        return super().retrieve(self, request, pk)
    

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        update_field = 'likes'
        inc_chapter_field.delay(pk, update_field)
        return Response({'message': 'Лайк поставлен'})
        

    
    
