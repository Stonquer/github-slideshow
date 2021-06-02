from django.urls import path
from one_card_wager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.one_card_intro, name="one_card_intro"),
    path("game/", views.one_card_wager, name="one_card_wager"),
    path("check/", views.one_card_wager, name="check"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)