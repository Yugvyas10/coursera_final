"""
URL configuration for littlelemon project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),

    # Djoser and Auth endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Direct /api/ aliases matching peer-review guidelines
    path('api/bookings/', include(router.urls)),
    path('api/menu/', views.MenuItemsView.as_view(), name='api-menu-list'),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view(), name='api-menu-detail'),
    path('api/menu-items/', views.MenuItemsView.as_view(), name='api-menu-items-list'),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='api-menu-items-detail'),
    path('api/registration/', include('djoser.urls')),
]
