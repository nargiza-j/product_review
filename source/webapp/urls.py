from django.urls import path

from webapp.views import ProductListView, ProductView, ProductAddView, ProductUpdateView, ProductDeleteView, \
    ReviewAddView, ReviewUpdateView, ReviewDeleteView, ReviewListView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('product/<int:pk>/', ProductView.as_view(), name="product_view"),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/reviews/add/', ReviewAddView.as_view(), name="product_add_review"),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name="review_update"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review_delete"),
    path('reviews/', ReviewListView.as_view(), name='review_list')
]