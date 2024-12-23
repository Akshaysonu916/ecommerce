from django.urls import path
from .views import home_view,add_products,signin_view,signup_view,logout_view,product_view,edit_product,delete_product,user_product_view


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
]
