from django.urls import path
from .views import MainPageView, BasePageView, PotravinyView, ProductCreateView, ProductUpdateView, ProductDeleteView, IndexView, SignUpView, CategoryView
from .views import PotravinyDetailedView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-view'),
    path('potraviny/', PotravinyView.as_view(), name='potraviny-view'),
    path('category/', CategoryView.as_view(), name='category-view'),
    path('base/', BasePageView.as_view(), name='base-view'),
    path('potraviny/create/', ProductCreateView.as_view(), name='potraviny-create-view'),
    path('potraviny/update/<int:pk>/', ProductUpdateView.as_view(), name='potraviny-update-view'),
    path('potraviny/delete/<int:pk>/', ProductDeleteView.as_view(), name='potraviny-delete-view'),
    path('index/', IndexView.as_view(), name='index-view'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/register/', SignUpView.as_view(), name='registration'),
    path('potraviny/<pk>', PotravinyDetailedView.as_view(), name='potraviny_detail'),
]