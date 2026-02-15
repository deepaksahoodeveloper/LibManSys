from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PermissionViewSet, UserViewSet, HistoricalUserViewSet, HistoricalGroupViewSet, HistoricalPermissionViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'permissions', PermissionViewSet, basename='permission')
router.register(r'users', UserViewSet, basename='user')
router.register(r'history/users', HistoricalUserViewSet, basename='historicaluser')
router.register(r'history/groups', HistoricalGroupViewSet, basename='historicalgroup')
router.register(r'history/permissions', HistoricalPermissionViewSet, basename='historicalpermission')

urlpatterns = router.urls