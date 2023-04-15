from rest_framework import serializers
from .models import Book, Chapter, Volume


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(source='chapter_set', many=True)

    class Meta:
        model = Volume
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    volume = VolumeSerializer(source='volume_set', many=True)

    class Meta:
        model = Book
        fields = '__all__'