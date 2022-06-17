from superadmin.views import SuperAdminViewSet
from rest_framework.routers import DefaultRouter
from superadmin import views

router = DefaultRouter()
router.register(r'superadmin', views.SuperAdminViewSet, basename='admin')
urlpatterns = router.urls