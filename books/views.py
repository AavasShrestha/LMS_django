from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from .services import BookService

class BookViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            service = BookService()
            book = service.add_book(serializer.validated_data)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        service = BookService()
        book = service.get_book_detail(pk)
        if isinstance(book, dict):  # If error message is returned
            return Response(book, status=status.HTTP_404_NOT_FOUND)
        return Response(BookSerializer(book).data)

    def update(self, request, pk=None):
        service = BookService()
        updated_data = request.data
        book = service.update_book(pk, updated_data)
        if isinstance(book, dict):  # If error message is returned
            return Response(book, status=status.HTTP_404_NOT_FOUND)
        return Response(BookSerializer(book).data)

    def destroy(self, request, pk=None):
        service = BookService()
        result = service.delete_book(pk)
        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        service = BookService()
        books = service.get_all_books()
        return Response(BookSerializer(books, many=True).data)
