from django.urls import include, path
from . import views
app_name='cart'


urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_details'),
    path('remove/<int:product_id>/',views.remove,name='cart_remove'),
     path('delete/<int:product_id>/',views.delete,name='cart_delete'),

   
]
