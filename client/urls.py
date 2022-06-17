from client.views import ClientViewSet
from rest_framework.routers import DefaultRouter
from client import views

router = DefaultRouter()
router.register(r'client', views.ClientViewSet, basename='customer')
urlpatterns = router.urls