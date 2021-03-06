from django.views.generic import DetailView, ListView
from rest_framework import generics
from product.serializers import *


class ProductView(ListView):
    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.order_by("-id")


class ProductDetail(DetailView):
    model = Product
    template_name = "product/product_detail.html"


class CategoryListView(ListView):
    model = Category
    template_name = "product/category.html"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "product/category_detail.html"


class ProductListApiView(generics.ListAPIView,
                         generics.CreateAPIView,
                         ):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# view for api
class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView,
                       generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'

# view for api
# class TestApiView(mixins.DestroyModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.ListModelMixin,
#                   generics.GenericAPIView):
#
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def list(self, request, *args,
#     **kwargs):
#         ...
#         return super().list(request, *args, **kwargs)
#
#     def perform_destroy(self, instance):
#         instance.logical_delete()


# view for REST API
# @csrf_exempt
# def product_list_api(request):
#     if request.method == 'GET':
#         product = Product.objects.all()
#         s = ProductSerializer(product, many=True)
#         return JsonResponse({
#             "products": s.data
#         })
#     elif request.method == 'POST':
#         s = ProductSerializer(data=request.POST)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.errors, status=400)
# view for api
