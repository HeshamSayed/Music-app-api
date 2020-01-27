from rest_framework import generics
from .models import Song
from .serializers import SongSerializer

class ListSongView(generics.ListAPIView):
    """
    it provides a get method handler
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer