from django.urls import path
from .views import MainPageView, BasePageView, PotravinyView, ProductCreateView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('', MainPageView.as_view(), name='main-view'),
    path('potraviny/', PotravinyView.as_view(), name='potraviny-view'),
    path('base/', BasePageView.as_view(), name='base-view'),
    path('potraviny/create/', ProductCreateView.as_view(), name='potraviny-create-view'),
    path('potraviny/update/<int:pk>/', ProductUpdateView.as_view(), name='potraviny-update-view'),
    path('potraviny/delete/<int:pk>/', ProductDeleteView.as_view(), name='potraviny-delete-view'),
]