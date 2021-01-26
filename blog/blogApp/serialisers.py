from rest_framework import serializers,permissions
from .models import Profile, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['name','city','following','followers']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['post_id','title','user','views','likes','content','created_on']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','content']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['comment_id','post_id','parent_id','likes','title','author','content','published_at']