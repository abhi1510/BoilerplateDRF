from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.ProductList.as_view()),
    url(r'^(?P<product_id>\w+)$', views.ProductDetails.as_view()),
]
