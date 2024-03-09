from django.urls import include, path
from . import views
app_name='searchapp'


urlpatterns = [
    path('',views.search,name='search'),
    
]
