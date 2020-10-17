from django.contrib import admin
from .models import Product, Category, Company, ProductSize, ProductSite, Comment, Image
from django.contrib.auth.models import Group


# admin.register() decorator
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content', )
    list_filter = ('category', )

#admin.site.register(Product, ProductAdmin) <- admin.site.register method

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)
admin.site.register(Image)

admin.site.unregister(Group)

admin.site.site_header = "Product Review Admin"

