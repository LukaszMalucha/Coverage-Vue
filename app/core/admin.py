from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ["email", "name"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}))
    # Page for adding new users
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)  # Coma - TUPLE!

class ProductModelAdmin(admin.ModelAdmin):
    ordering = ["product_name", "product_brand", "product_code", "product_category", "business"]
    list_display = ["product_name", "business"]
    search_fields = ["product_name","product_brand", "product_code"]
    list_filter = ("product_brand",)

    class Meta:
        model = models.ProductModel

class DocumentModelAdmin(admin.ModelAdmin):
    ordering = ["document_title", "document_created_at", "document_last_edition"]
    list_display = ["document_title", "product", "document_created_at" ]
    search_fields = ["document_title",]
    list_filter = ("document_brand",)

    class Meta:
        model = models.DocumentModel

class TopicModelAdmin(admin.ModelAdmin):
    ordering = ["topic_title", "document", "topic_last_edition"]
    list_display = ["topic_title", "document", "topic_last_edition"]
    search_fields = ["topic_title", "document__document_title"]

    class Meta:
        model = models.TopicModel


admin.site.register(models.User, UserAdmin)
admin.site.register(models.MyProfile)
admin.site.register(models.ProductModel, ProductModelAdmin)
admin.site.register(models.DocumentModel, DocumentModelAdmin)
admin.site.register(models.TopicModel, TopicModelAdmin)

