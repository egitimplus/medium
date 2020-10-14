from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
