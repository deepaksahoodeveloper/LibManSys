from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.models import Group
from simple_history import register

register(Group, m2m_fields=['permissions'])
register(Permission)
register(User, m2m_fields=['groups', 'user_permissions'])