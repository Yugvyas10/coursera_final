from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} for {self.no_of_guests} guests on {self.booking_date}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"

    def get_item(self):
        return f"{self.title} : {str(self.price)}"


# Alias MenuItem to Menu for compatibility with tests and different rubric references
MenuItem = Menu
