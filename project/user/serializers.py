from rest_framework import serializers
from django.contrib.auth.models import Group, Permission, User

# Get historical models dynamically
HistoricalUser = User.history.model
HistoricalGroup = Group.history.model
HistoricalPermission = Permission.history.model

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class HistoricalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalUser
        fields = '__all__'


class HistoricalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalGroup
        fields = '__all__'


class HistoricalPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPermission
        fields = '__all__'