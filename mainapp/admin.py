from django.contrib import admin
from mainapp.models import Category, Group, Subgroup, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    list_filter = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Group, GroupAdmin)

class SubgroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'slug']
    list_filter = ['name', 'group']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Subgroup, SubgroupAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'subgroup', 'slug']
    list_filter = ['name', 'subgroup']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)