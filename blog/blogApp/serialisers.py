from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['']