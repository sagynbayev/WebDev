from django.http.response import JsonResponse
from api.models import Product
from api.models import Category
def productList(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    print(products_json)
    return JsonResponse(products_json, safe=False)

def productDetail(request, productId):
    try:
        product = Product.objects.get(id = productId)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(product.to_json())

def categoryList(request):
    categories = Category.objects.all()
    categories_json = [category.to_json1() for category in categories]
    print(categories_json)
    return JsonResponse(categories_json, safe=False)

def categoryDetail(request, categoryId):
    try:
        category = Category.objects.get(id = categoryId)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(category.to_json1())