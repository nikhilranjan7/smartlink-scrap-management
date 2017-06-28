from django.contrib import admin
from scr.models import Category, Quote, trxn_m
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Category)
admin.site.register(Quote)


class Category_list(resources.ModelResource):

    class Meta:
        model = Category

class Quote_list(resources.ModelResource):

    class Meta:
        model = Quote

class trx_list(resources.ModelResource):

    class Meta:
        model = trxn_m
