from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('darknet_app', views.ProductsView)
urlpatterns = [
    path('', include(router.urls)),
]