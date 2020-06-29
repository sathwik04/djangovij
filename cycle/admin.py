from django.contrib import admin
from.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
@admin.register(Bills)
class BillsAdmin(ImportExportModelAdmin):
    pass

