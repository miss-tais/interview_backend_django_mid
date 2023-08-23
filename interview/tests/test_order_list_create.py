from datetime import datetime, timedelta

import pytest

from django.urls import reverse
from rest_framework import status

from .base import BaseDBTestCase


class TestOrderListCreateView(BaseDBTestCase):

    url_name = 'order-list'

    @pytest.mark.parametrize('start_from,embargo_before,expected_results_num', [
        ((datetime.now() + timedelta(days=20)).date(), None, 0),
        ((datetime.now() + timedelta(days=10)).date(), None, 2),
        (None, (datetime.now() + timedelta(days=40)).date(), 5),
        (None, (datetime.now() + timedelta(days=20)).date(), 1),
        ((datetime.now() + timedelta(days=10)).date(), (datetime.now() + timedelta(days=40)).date(), 2),
        ((datetime.now() + timedelta(days=10)).date(), (datetime.now() + timedelta(days=20)).date(), 0),
        ('', '', 5),
    ])
    def test_filter_orders(self, client, start_from, embargo_before, expected_results_num):
        query_params = {}

        if start_from is not None:
            query_params['start_date__gte'] = start_from

        if embargo_before is not None:
            query_params['embargo_date__lte'] = embargo_before

        response = client.get(reverse(self.url_name), query_params)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == expected_results_num
