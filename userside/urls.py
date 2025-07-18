from django.urls import path
from .views import *


urlpatterns = [
    path('',home_view,name='home'),
    path('addproducts/',add_products,name='addproducts'),
    path('signin/',signin_view,name='signin'),
    path('signup/',signup_view,name='signup'),
    path('signout/',logout_view,name='signout'),
    path('products/',product_view,name='products'),
    path('edit_product/<int:id>/',edit_product,name='edit_product'),
    path('delete_product/<int:id>/',delete_product,name='delete_product'),
    path('userproduct/',user_product_view,name='userproduct'),

    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    #cart urls
    path('cart/',view_cart, name='view_cart'),
    # path('cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:pk>/',add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/',remove_from_cart, name='remove_from_cart'),

    #payment urls
    # path('buy/<int:product_id>/', buy_now, name='buy_now'),
    # path('thank-you/', thank_you, name='thank_you'),
    path('order/<int:product_id>/', place_order, name='place_order'),
    path('order-success/', order_success, name='order_success'),
]