from rest_framework import serializers
from .models import Author, Post



class PostSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author.name')
    author_name = serializers.StringRelatedField(source='author.name')
    # author = AuthorSerializer('author', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author_name')

class AuthorSerializer(serializers.ModelSerializer):
    # posts = serializers.StringRelatedField(many=True)
    posts = PostSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'posts')

    def create(self, validated_data):
        posts_data = validated_data.pop("posts")
        author = Author.objects.create(**validated_data)
        for post_data in posts_data:
            Post.objects.create(author=author, **post_data)
        return author         