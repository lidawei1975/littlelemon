from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer



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