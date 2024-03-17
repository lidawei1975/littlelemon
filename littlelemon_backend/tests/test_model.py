from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80.49, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80.49")