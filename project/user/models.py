from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.models import Group
from simple_history import register

register(Group)
register(Permission)
register(User)