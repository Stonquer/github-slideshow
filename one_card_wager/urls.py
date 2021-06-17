from django.urls import path
from one_card_wager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.one_card_intro, name="one_card_intro"),
    path("game/", views.one_card_wager, name="one_card_wager"),
    path("game/check/", views.check, name="check"),
    path("game/check/showdown/", views.showdown, name="showdown"),
    path("game/check/fold/", views.fold, name="fold"),
    path("game/bet/", views.bet, name="bet"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

