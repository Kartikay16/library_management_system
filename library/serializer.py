from rest_framework import serializers

class BooksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    genre = serializers.CharField(max_length = 200)
    is_available = serializers.BooleanField(default=True)

