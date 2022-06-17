
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geo/', include("geocalisation.urls")),
    # path('dashboard/', include("dashboard.urls")),
    # path('recommandation/', include("recommandation.urls")),
    path('auth/', include("authentification.urls")),
    path('part/', include("partenaire.urls")),
    path('customer/', include("client.urls")),
     path('administrateur/', include("superadmin.urls")),




]
