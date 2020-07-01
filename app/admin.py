from django.contrib import admin
from app.models import Category, Product, Tag
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'descricao', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_active', 'get_tags']
    list_filter = ['is_active']
    search_fields = ['name']

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)