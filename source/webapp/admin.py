from django.contrib import admin

# Register your models here.
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    fields = ['name', 'description', 'category', 'picture']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', "rate"]
    list_display_links = ['id', 'author']
    fields = ['author', 'content', 'product', 'rate', 'moderated', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
