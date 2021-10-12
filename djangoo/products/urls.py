from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path('create', views.product_create_view),
    path('product', views.product_detail_view),

]
