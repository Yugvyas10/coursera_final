from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    """Serve static HTML landing page for Little Lemon restaurant."""
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    """
    Handles GET (list menu items) and POST (create menu item).
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Handles GET (retrieve single item), PUT (update), and DELETE (delete).
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for table bookings.
    Secured with token authentication: only authenticated users can access.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
