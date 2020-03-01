from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from daterange_filter.filter import DateRangeFilter

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    list_filter = ("is_active", "is_staff", "is_superuser", "is_vip")
    search_fields = ["email", "name"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "is_vip")}),
        (_("Important dates"), {"fields": ("last_login",)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)  # Coma - TUPLE!

class ProductModelAdmin(admin.ModelAdmin):
    ordering = ["product_name", "product_brand", "product_code", "product_category", "business"]
    list_display = ["product_name", "product_brand", "product_code", "product_category", "business"]
    search_fields = ["product_name","product_brand", "product_name", "product_code"]
    list_filter = ("product_brand",)

    class Meta:
        model = models.ProductModel

class DocumentModelAdmin(admin.ModelAdmin):
    ordering = ["document_title", "document_created_at", "document_last_edition"]
    list_display = ["document_title", "document_created_at", "document_last_edition"]
    search_fields = ["document_title",]

    class Meta:
        model = models.DocumentModel


admin.site.register(models.MyProfile)
admin.site.register(models.ProductModel, ProductModelAdmin)
admin.site.register(models.DocumentModel, DocumentModelAdmin)

