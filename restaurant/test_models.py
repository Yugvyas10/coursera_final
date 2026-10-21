from django.test import TestCase
from decimal import Decimal
from restaurant.models import Menu, MenuItem, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        self.assertEqual(item.get_item(), "IceCream : 80")

    def test_menu_creation_with_decimal(self):
        item = Menu.objects.create(title="Greek Salad", price=Decimal("12.99"), inventory=40)
        self.assertEqual(item.title, "Greek Salad")
        self.assertEqual(item.price, Decimal("12.99"))
        self.assertEqual(item.inventory, 40)


class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date="2026-10-20T18:00:00Z"
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
        self.assertIn("John Doe", str(booking))
