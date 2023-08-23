import pytest

from django.urls import reverse
from rest_framework import status

from .base import BaseDBTestCase


class TestInventoryListCreateView(BaseDBTestCase):

    url_name = 'inventory-list'

    @pytest.mark.parametrize('limit,offset,expected_results_num', [
        (3, None, 3),
        (3, 3, 3),
    ])
    def test_filter_inventory(self, client, limit, offset, expected_results_num):
        query_params = {}

        if limit:
            query_params['limit'] = limit

        if offset:
            query_params['offset'] = offset

        response = client.get(reverse(self.url_name), query_params)

        assert response.status_code == status.HTTP_200_OK

        assert 'count' in response.data
        assert response.data['count'] == 17

        assert 'results' in response.data
        assert len(response.data['results']) == expected_results_num
