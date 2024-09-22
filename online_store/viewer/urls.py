from django.urls import path
from .views import MainPageView, BasePageView, PotravinyView


urlpatterns = [
    path('', MainPageView.as_view(), name='main-view'),
    path('potraviny/', PotravinyView.as_view(), name='potraviny-view'),
    path('base/', BasePageView.as_view(), name='base-view'),  # Nastavení hlavní stránky
]
