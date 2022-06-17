from partenaire.views import PartnerViewSet
from rest_framework.routers import DefaultRouter
from partenaire import views

router = DefaultRouter()
router.register(r'partner', views.PartnerViewSet, basename='partenaire')
urlpatterns = router.urls