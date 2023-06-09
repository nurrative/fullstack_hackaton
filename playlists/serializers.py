from rest_framework.serializers import ModelSerializer
from .models import *
from songs.serializers import SimpleSongSerializer
from review.serializers import CommentSerializer


class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        exclude = ('user', 'song')

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = {
            'id': instance.user.id,
            'email': instance.user.email,
        }
        rep['likes'] = instance.likes.all().count()
        rep['rating'] = instance.average_rating
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        songs_data = SongSerializer(instance.song.all(), many=True).data
        songs_data = [{**song, 'audio_file': f"{config('LINK')}{song['audio_file']}"} for song in songs_data]
        rep['songs'] = songs_data
        return rep


class SimplePlaylist(ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'cover_photo')
