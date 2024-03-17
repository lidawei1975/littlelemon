from django.test import TestCase, RequestFactory
from .models import Menu
from .views import MenuItemView
from .serializers import MenuSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80.49, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80.49")


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(
            Title="Main1",
            Price=9.49,
            Inventory=2
        )
        Menu.objects.create(
            Title="Main2",
            Price=11.50,
            Inventory=1
        )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)