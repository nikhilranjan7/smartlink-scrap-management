from django.contrib import admin
from scr.models import Category, Quote, Random_m
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(Random_m)

class Category_list(resources.ModelResource):

    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = Category_list

class Quote_list(resources.ModelResource):

    class Meta:
        model = Quote


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = Quote_list
