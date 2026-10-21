from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-items-detail'),
    path('booking/', include(router.urls)),
]
