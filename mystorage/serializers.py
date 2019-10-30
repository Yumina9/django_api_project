from rest_framework import serializers

from .models import Album, Files, Essay


class AlbumSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'author', 'image', 'desc')

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')


class FilesSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    files = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk', 'author', 'files', 'desc')
