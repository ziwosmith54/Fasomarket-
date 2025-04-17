from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('annonces/', include('annonces.urls')),
    path('messages/', include('messagerie.urls')),
    path('paiement/', include('paiement.urls')),
    path('dashboard/', include('dashboard.urls')),
]
