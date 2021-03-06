from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact"),
    path('tracker/', views.tracker, name="Tracker"),
    path('search/', views.search, name="Search"),
    path('productview/<int:pid>', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Chekout"),
    path('handlerequest/', views.handle_request, name="HandleRequest")
]