from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.models import Content, Channel
from channels.serializers import ContentSerializer, ChannelSerializer, ContentSerializerPost, ChannelSerializerPost
from rest_framework import viewsets
# Create your views here.

# @api_view(['GET'])
# def all_contents(request):
#     return Response(serializers.serialize('json',Content.objects.all()))

# @api_view(['GET'])
# def all_channels(request):
#     return Response(serializers.serialize('json',Channel.objects.all()))

# class ChannelList(APIView):

#     def get(self, request, format = None):
#         channels = Channel.objects.all()
#         serializer = ChannelSerializer(channels, many=True)
#         return Response(serializer.data)

#     def post(self, request, format = None):
#         serializer = ChannelSerializer(data = request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except ValidationError as err:
#                 return Response(err.messages, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ContentList(APIView):

#     def get(self, request, format = None):
#         contents = Content.objects.all()
#         serializer = ContentSerializer(contents, many=True)
#         return Response(serializer.data)

#     def post(self, request, format = None):
#         serializer = ContentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContentViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return ContentSerializerPost
        return ContentSerializer

    queryset = Content.objects.all()

class ChannelViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return ChannelSerializerPost
        return ChannelSerializer

    queryset = Channel.objects.all()





