from datetime import datetime, timedelta

import pytest

from django.urls import reverse
from rest_framework import status

from .base import BaseDBTestCase


class TestInventoryListCreateView(BaseDBTestCase):

    url_name = 'inventory-list'

    @pytest.mark.parametrize('created_from,expected_results_num', [
        ((datetime.now() + timedelta(days=1)).date(), 0),
        ('', 17),
        ((datetime.now() - timedelta(days=1)).date(), 17),
    ])
    def test_filter_inventory(self, client, created_from, expected_results_num):
        response = client.get(reverse(self.url_name), {'created_at__gte': created_from})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == expected_results_num
