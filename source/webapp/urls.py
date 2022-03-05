from django.urls import path

from webapp.views import ProductListView, ProductView, ProductAddView, ProductUpdateView, ProductDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('product/<int:pk>/', ProductView.as_view(), name="product_view"),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]