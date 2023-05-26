from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SongSerializer, ArtistSerializer, AlbumSerializer
from .models import Song, Artist, Album
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from drf_yasg.utils import swagger_auto_schema


class SongUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema()
    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtistListCreateAPIView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'id'

#
# class ArtistDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     lookup_field = 'id'

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

