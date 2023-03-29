from rest_framework import serializers
from channels.models import Channel,Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'files', 'type_file', 'name', 'description', 'authors', 'rating','channel']

class ContentSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'files', 'type_file', 'name', 'description', 'authors', 'rating']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'language', 'picture', 'content', 'parent','children']

class ChannelSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'language', 'picture', 'content', 'parent']