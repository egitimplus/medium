from .serializers import ProductSerializer, ImageSerializer
from .models import Product, Image
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Product.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_related('sites')

        if is_expanded(self.request, 'company'):
            queryset = queryset.prefetch_related('sites__company')

        if is_expanded(self.request, 'productsize'):
            queryset = queryset.prefetch_related('sites__productsize')

        return queryset


class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
