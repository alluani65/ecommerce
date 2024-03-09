from django.urls import include, path
from . import views
app_name='ecommerceapp'


urlpatterns = [
    path('',views.allproductscat,name='allproductscat'),
    path('<slug:cslug>/',views.allproductscat,name='product_by_category'),
    path('<slug:cslug>/<slug:pslug>/',views.productdetail,name='product_detail')
]
