from django.urls import path
from .views import MainPageView, BasePageView, PotravinyView, ProductCreateView, ProductUpdateView, ProductDeleteView, IndexView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-view'),
    path('potraviny/', PotravinyView.as_view(), name='potraviny-view'),
    path('base/', BasePageView.as_view(), name='base-view'),
    path('potraviny/create/', ProductCreateView.as_view(), name='potraviny-create-view'),
    path('potraviny/update/<int:pk>/', ProductUpdateView.as_view(), name='potraviny-update-view'),
    path('potraviny/delete/<int:pk>/', ProductDeleteView.as_view(), name='potraviny-delete-view'),
    path('index/', IndexView.as_view(), name='index-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]
