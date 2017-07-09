from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from models import Category, Quote, trxn_m


class CategorylistResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoriesAdmin(ImportExportModelAdmin):
    resource_class = CategorylistResource


class QuotelistResource(resources.ModelResource):
    class Meta:
        model = Quote


class QuoteListAdmin(ImportExportModelAdmin):
    resource_class = QuotelistResource


class trxlistResource(resources.ModelResource):
    class Meta:
        model = trxn_m


class trxListAdmin(ImportExportModelAdmin):
    resource_class = trxlistResource


admin.site.register(Category, CategoriesAdmin)
admin.site.register(Quote,QuoteListAdmin)
admin.site.register(trxn_m, trxListAdmin)
