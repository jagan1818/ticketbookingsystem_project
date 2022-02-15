from shows.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


class MoviesList(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['screen__theatre__city']


class AddMovies(APIView):
    def post(self, request):
        movie = MoviesSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response({"status": "success", "data": movie.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": movie.errors}, status=status.HTTP_400_BAD_REQUEST)


class UpdateMovies(APIView):
    def patch(self, request, id=None):
        movie = Movies.objects.get(id=id)
        movie_serializer = MoviesSerializer(movie, data=request.data, partial=True)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response({"status": "success", "data": movie_serializer.data})
        else:
            return Response({"status": "error", "data": movie_serializer.errors})



