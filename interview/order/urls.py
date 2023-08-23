from django.urls import path

from interview.order.views import OrderDestroyView, OrderListCreateView, OrderTagListCreateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDestroyView.as_view(), name='order-destroy'),

]