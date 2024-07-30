from django.urls import path
from .views import register, profile, product_list, product_detail, add_to_cart, cart_detail, checkout, payment, order_history, admin_order_management

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('orders/', order_history, name='order_history'),
    path('admin/orders/', admin_order_management, name='admin_order_management'),
]
