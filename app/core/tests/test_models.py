from django.contrib.auth import get_user_model
from django.test import TestCase

from core.models import MyProfile, ProductModel, DocumentModel, TopicModel


class UserModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )
        self.user_1 = get_user_model().objects.create_user(
            email="test1@GMAIL.COM",
            password="test1234",
            name="Test User 1"
        )

        self.user_superuser = get_user_model().objects.create_superuser(
            email="superuser@gmail.com",
            password="test1234",
        )

    def tearDown(self):
        self.user.delete()
        self.user_1.delete()
        self.user_superuser.delete()

    def test_email(self):
        self.assertEqual(self.user.email, "test@gmail.com")

    def test_new_user_email_normalized(self):
        """Test if the email for a new user is normalized"""
        self.assertEqual(self.user_1.email, "test1@gmail.com")

    def test_new_user_empty_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test1234")

    def test_name(self):
        self.assertEqual(self.user.name, "Test User")

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), 'test@gmail.com')

    def test_superuser_name(self):
        self.assertEqual(self.user_superuser.name, "Admin")

    def test_password(self):
        self.assertTrue(self.user.check_password("test1234"))

    def test_new_user_invalid_password(self):
        """Test creating user with password too short"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test")

    def test_new_user_empty_password(self):
        """Test creating user with no password"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("test3@gmail.com", "")

    def test_new_user_has_usable_password(self):
        self.assertTrue(self.user.has_usable_password())

    def test_last_login_default(self):
        self.assertIsNone(self.user.last_login)

    def test_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_str(self):
        self.assertEqual(str(self.user), "test@gmail.com")

    def test_id(self):
        self.assertEqual(self.user.id, 1)

    def test_is_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_superuser_is_staff(self):
        self.assertTrue(self.user_superuser.is_staff)

    def test_is_superuser(self):
        self.assertFalse(self.user.is_superuser)

    def test_superuser_is_superuser(self):
        self.assertTrue(self.user_superuser.is_superuser)

    def test_is_anonymous(self):
        self.assertFalse(self.user.is_anonymous)

    def test_hash(self):
        self.assertEqual(hash(self.user), hash(self.user.id))

    def test_user_permissions(self):
        self.assertFalse(self.user.user_permissions.exists())

    def test_get_group_permissions(self):
        self.assertEqual(len(self.user.get_group_permissions()), 0)

    def test_get_all_permissions(self):
        self.assertEqual(len(self.user.get_all_permissions()), 0)

    def test_has_perm(self):
        self.assertFalse(self.user.has_perm('test_perm'))

    def test_has_perms(self):
        self.assertFalse(self.user.has_perms(['test_perm']))

    def test_has_module_perms(self):
        self.assertFalse(self.user.has_module_perms('test_module'))


class MyProfileModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )
        self.user_1 = get_user_model().objects.create_user(
            email="test1@gmail.com",
            password="test1234",
            name=""
        )
        self.my_profile = MyProfile.objects.filter(owner__email="test@gmail.com").first()
        self.my_profile_1 = MyProfile.objects.filter(owner__email="test1@gmail.com")

    def tearDown(self):
        self.user.delete()
        self.user_1.delete()
        self.my_profile.delete()
        self.my_profile_1.delete()

    def test_my_profile_str(self):
        self.assertEqual(str(self.my_profile), "test@gmail.com profile")

    def test_my_profile_created(self):
        self.assertTrue(self.my_profile_1.exists())

    def test_single_profile_created(self):
        self.assertEqual(len(MyProfile.objects.filter(owner__email="test@gmail.com")), 1)

    def test_my_profile_position(self):
        self.assertEqual(self.my_profile.position, "guest")

    def test_my_profile_image(self):
        self.assertEqual(str(self.my_profile.image)[10:], "default.jpg")

    def test_my_profile_owner(self):
        self.assertEqual(str(self.my_profile.owner), "test@gmail.com")

    def test_my_profile_str(self):
        self.assertEqual(str(self.my_profile), "test@gmail.com profile")

    def test_my_profile_verbose_name(self):
        self.assertEqual(self.my_profile._meta.verbose_name, "User Profile")

    def test_my_profile_verbose_name_plural(self):
        self.assertEqual(self.my_profile._meta.verbose_name_plural, "User Profiles")


class ProductModelTest(TestCase):

    def setUp(self):
        self.product = ProductModel.objects.create(
            product_identifier="Test",
            product_name="test",
            product_brand="12",
            product_category="test",
            product_code="test",
            product_series="12",
            product_part_number="test",
            business="Test",
        )
        self.empty_product = ProductModel.objects.create()

    def tearDown(self):
        self.product.delete()
        self.empty_product.delete()

    def test_creating_product(self):
        self.assertTrue(self.product)

    def test_creating_empty_company(self):
        self.assertTrue(self.empty_product)

    def test_product_str(self):
        self.assertEqual(str(self.product), "test")

    def test_product_verbose_name(self):
        self.assertEqual(self.product._meta.verbose_name_plural, "Products")


class DocumentModelTest(TestCase):

    def setUp(self):
        self.product = ProductModel.objects.create(
            product_identifier="Test",
            product_name="test",
            product_brand="12",
            product_category="test",
            product_code="test",
            product_series="12",
            product_part_number="test",
            business="Test",
        )

        self.document = DocumentModel.objects.create(
            document_title="Test",
            document_number="Test",
            document_part_number="Test",
            document_version="Test",
            document_revision="Test",
            document_type="Test",
            document_lang="Test",
            document_created_at="2020-01-01",
            document_last_edition="2020-01-01",
            document_last_publication="2020-01-01",
            document_revised_modified="2020-01-01",
            document_brand="Test",
            document_link="Test",
            maps_link="Test",
            product=self.product,
            document_identifier="Test",
        )

    def tearDown(self):
        self.document.delete()

    def test_creating_document(self):
        self.assertTrue(self.document)

    def test_document_str(self):
        self.assertEqual(str(self.document), "Test")

    def test_document_verbose_name(self):
        self.assertEqual(self.document._meta.verbose_name_plural, "Documents")


class TopicModelTest(TestCase):

    def setUp(self):
        self.product = ProductModel.objects.create(
            product_identifier="Test",
            product_name="test",
            product_brand="12",
            product_category="test",
            product_code="test",
            product_series="12",
            product_part_number="test",
            business="Test",
        )
        self.document = DocumentModel.objects.create(
            document_title="Test",
            document_number="Test",
            document_part_number="Test",
            document_version="Test",
            document_revision="Test",
            document_type="Test",
            document_lang="Test",
            document_created_at="2020-01-01",
            document_last_edition="2020-01-01",
            document_last_publication="2020-01-01",
            document_revised_modified="2020-01-01",
            document_brand="Test",
            document_link="Test",
            maps_link="Test",
            product=self.product,
            document_identifier="Test",
        )
        self.topic = TopicModel.objects.create(
            topic_title="Test",
            topic_breadcrumb="Test",
            topic_depth=2,
            topic_last_edition="2020-01-01",
            topic_link="Test",
            document=self.document
        )

    def tearDown(self):
        self.topic.delete()

    def test_creating_topic(self):
        self.assertTrue(self.topic)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Test")

    def test_topic_verbose_name(self):
        self.assertEqual(self.topic._meta.verbose_name_plural, "Document Topics")
