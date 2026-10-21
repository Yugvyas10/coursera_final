from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.item1 = Menu.objects.create(title="Pizza", price=Decimal("12.99"), inventory=20)
        self.item2 = Menu.objects.create(title="Pasta", price=Decimal("14.50"), inventory=15)
        self.item3 = Menu.objects.create(title="Salad", price=Decimal("8.00"), inventory=30)

    def test_getall(self):
        """Retrieve all Menu objects and verify against serialized data."""
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_item(self):
        """Retrieve a single menu item."""
        response = self.client.get(f'/restaurant/menu/{self.item1.pk}')
        serializer = MenuSerializer(self.item1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='bookinguser',
            password='bookingpassword123'
        )

    def test_unauthenticated_booking_access(self):
        """Verify unauthenticated requests cannot access the booking API."""
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_booking_access(self):
        """Verify authenticated requests can access and create bookings."""
        self.client.force_authenticate(user=self.user)
        create_response = self.client.post('/restaurant/booking/tables/', {
            'name': 'Alice Smith',
            'no_of_guests': 2,
            'booking_date': '2026-10-21T19:30:00Z'
        })
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        list_response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list_response.data), 1)


class StaticPageViewTest(TestCase):
    def test_index_view(self):
        """Verify static HTML template is served correctly."""
        response = self.client.get('/restaurant/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Little Lemon")
        self.assertTemplateUsed(response, "index.html")
