from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Create your serializers here.
from snippets.models import Snippet


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'snippets']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'email']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
