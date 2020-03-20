from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from core.utils import content_file_name


# Manager Class
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError("User must have a valid email address")
        if len(str(password)) < 8:
            raise ValueError("This password is too short. It must contain at least 8 characters.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.name = "Admin"
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Model Class
class User(AbstractBaseUser, PermissionsMixin):
    """Customized user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        MyProfile.objects.get_or_create(owner=self)


class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default="guest", blank=True)
    image = models.ImageField(upload_to=content_file_name, default="portraits/default.jpg")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"


class ProductModel(models.Model):
    """Model for Products"""
    product_identifier = models.CharField(max_length=254, unique=True, blank=False)
    product_name = models.CharField(max_length=254, default="Not Specified", blank=True)
    product_brand = models.CharField(max_length=254, default="Not Specified", blank=True)
    product_category = models.CharField(max_length=254, default="Not Specified", blank=True)
    product_code = models.TextField(default="Not Specified")
    product_series = models.CharField(max_length=254, default="Not Specified", blank=True)
    product_part_number = models.CharField(max_length=254, default="Not Specified", blank=True)
    business = models.CharField(max_length=254, default="Not Specified", blank=True)
    uploaded = models.DateTimeField(default=datetime.today().strftime('%Y-%m-%d'))

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name


class DocumentModel(models.Model):
    """Model for Document"""
    document_title = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_number = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_part_number = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_version = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_revision = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_type = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_lang = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_created_at = models.DateField(blank=True)
    document_last_edition = models.DateField(blank=True)  # REMEMBER TO RELATE IT LATER TO TOPIC MODIFICATION
    document_last_publication = models.DateField(blank=True)
    document_revised_modified = models.DateField(blank=True)
    document_brand = models.CharField(max_length=254, default="Not Specified", blank=True)
    document_link = models.CharField(max_length=254, default="Not Specified", blank=True)
    maps_link = models.CharField(max_length=254, default="Not Specified", blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    document_identifier = models.CharField(max_length=254, blank=False, unique=True)

    uploaded = models.DateTimeField(default=datetime.today().strftime('%Y-%m-%d'))

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.document_title


class TopicModel(models.Model):
    """Model for Document Topics"""
    topic_title = models.CharField(max_length=254, default="Not Specified", blank=True)
    topic_breadcrumb = models.TextField(default="Not Specified")
    topic_depth = models.IntegerField(blank=False, default=0)  # Keep zero for later QA checks
    topic_last_edition = models.DateField(blank=True)
    topic_link = models.CharField(max_length=254, default="Not Specified", blank=True)
    document = models.ForeignKey(DocumentModel, on_delete=models.CASCADE, related_name="topics")
    uploaded = models.DateTimeField(default=datetime.today().strftime('%Y-%m-%d'))

    objects = models.Manager()

    class Meta:
        verbose_name = "Document Topic"
        verbose_name_plural = "Document Topics"

    def __str__(self):
        return self.topic_title
