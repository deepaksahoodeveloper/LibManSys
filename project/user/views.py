from rest_framework import viewsets
from django.contrib.auth.models import Group, Permission, User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import GroupSerializer, PermissionSerializer,UserSerializer, HistoricalUserSerializer, HistoricalGroupSerializer, HistoricalPermissionSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Get historical models dynamically
HistoricalUser = User.history.model
HistoricalGroup = Group.history.model
HistoricalPermission = Permission.history.model

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class HistoricalUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoricalUser.objects.all().order_by('-history_date')
    serializer_class = HistoricalUserSerializer

class HistoricalGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoricalGroup.objects.all().order_by('-history_date')
    serializer_class = HistoricalGroupSerializer

class HistoricalPermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoricalPermission.objects.all().order_by('-history_date')
    serializer_class = HistoricalPermissionSerializer