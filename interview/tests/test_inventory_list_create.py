import json

from django.urls import reverse
from rest_framework import status

from interview.inventory.models import Inventory
from .base import BaseDBTestCase


class TestInventoryListCreateView(BaseDBTestCase):

    url_name = 'inventory-list'

    def test_post_create_inventory(self, client):
        data = {
            "name": "test_1",
            "type": {
                "name": "test_1",
            },
            "language": {
                "name": "test_1",
            },
            "tags": [
                {
                    "name": "test_1",
                    "is_active": True,
                },
                {
                    "name": "test_2",
                    "is_active": False,
                },
            ],
            "metadata": {
                "year": 2000,
                "actors": ["test_1", "test_1"],
                "imdb_rating": '2.22',
                "rotten_tomatoes_rating": 5,
            },
        }

        response = client.post(reverse(self.url_name), data, content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED

        inventory = Inventory.objects.get(id=response.data['id'])

        assert inventory.type.name == data['type']['name']
        assert inventory.language.name == data['language']['name']
        assert len(inventory.tags.all()) == 2
        assert len(inventory.tags.filter(is_active=True)) == 1
        assert len(inventory.tags.filter(is_active=False)) == 1

        assert json.loads(inventory.metadata) == data['metadata']
