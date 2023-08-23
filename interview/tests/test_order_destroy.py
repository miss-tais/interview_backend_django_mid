from django.urls import reverse
from rest_framework import status

from interview.order.models import Order

from .base import BaseDBTestCase


class TestOrderDestroyView(BaseDBTestCase):

    url_name = 'order-destroy'

    def test_destroy(self, client):
        order = Order.objects.first()

        assert order.is_active

        response = client.delete(reverse(self.url_name, args=(order.pk, )))
        assert response.status_code == status.HTTP_204_NO_CONTENT

        order.refresh_from_db()

        assert not order.is_active
