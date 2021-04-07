from django.urls import path, re_path
from api.views import productList, productDetail, categoryList, categoryDetail
urlpatterns = [
    path('products/', productList),
    path('products/<int:productId>/', productDetail),
    path('categories/', categoryList),
    path('categories/<int:categoryId>', categoryDetail)
]