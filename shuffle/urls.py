from django.urls import path
from shuffle import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path("", views.shuffle, name="shuffle"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)