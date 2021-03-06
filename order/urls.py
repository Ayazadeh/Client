from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('buy/<int:pk>', BuyView.as_view(), name='buy'),
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>', remove_from_cart, name='remove-from-cart'),
    path('cart/', Cart.as_view(), name='cart'),
    path('all/api', OrderListApi.as_view(), name='order_all_api'),
    path('api/<int:pk>', OrderDetailApi.as_view(), name='order_detail_api'),
]
