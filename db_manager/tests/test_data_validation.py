import os

import pandas as pd
from django.conf import settings
from django.test import TestCase

from db_manager.data_validation import validate_documents_dataset, validate_products_dataset, validate_topics_dataset
from db_manager.data_validation import products_dataset_check, documents_dataset_check, topics_dataset_check

dataset_test_path = os.path.join(settings.BASE_DIR, "db_manager/tests/dataset_test.csv")
dataset_test_documents_path = os.path.join(settings.BASE_DIR, "db_manager/tests/dataset_test_documents.csv")
dataset_test_topic_path = os.path.join(settings.BASE_DIR, "db_manager/tests/dataset_test_topics.csv")

def dataset_test():
    dataset = pd.read_csv(dataset_test_path, encoding="utf-8-sig")

    return dataset

def dataset_test_documents():
    dataset = pd.read_csv(dataset_test_documents_path, encoding="utf-8-sig")

    return dataset

def dataset_test_topics():
    dataset = pd.read_csv(dataset_test_topic_path, encoding="utf-8-sig")

    return dataset


def dataset_test_erratic():
    dataset = pd.read_csv(dataset_test_path, encoding="utf-8-sig")
    dataset.loc[len(dataset)] = [1, 2, 3, 4, 5, 6, 7]

    return dataset

def dataset_test_erratic_columns():
    dataset = pd.read_csv(dataset_test_path, encoding="utf-8-sig")
    dataset.loc[len(dataset)] = [1, 2, 3, 4, 5, 6, 7]
    dataset["erratic"] = "erratic"
    return dataset

class ValidateProductsDatasetTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()
        self.dataset_test_erratic = dataset_test_erratic()
        self.dataset_test_erratic_columns = dataset_test_erratic_columns()


    def test_validate_products_dataset(self):
        validate = validate_products_dataset(self.dataset_test)
        self.assertEqual(len(validate), 2)

    def test_validate_products_dataset_erratic(self):
        validate = validate_products_dataset(self.dataset_test_erratic)
        self.assertEqual(len(validate), 2)
        self.assertEqual(validate[1], "Some product identifiers length is not equal to  40 characters. Count: 5")

    def test_validate_products_dataset_erratic_columns(self):
        validate = validate_products_dataset(self.dataset_test_erratic_columns)
        self.assertEqual(len(validate), 1)


class ProductsDatasetCheckTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()



    def test_products_dataset_check(self):
        check = products_dataset_check(self.dataset_test)
        self.assertEqual(len(check),  2)
        self.assertEqual(check[0][0]["name"], "Product Name")
        self.assertEqual(check[0][0]["Longest String"], "TEST44")
        self.assertEqual(check[0][0]["Shortest String"], "T")
        self.assertEqual(check[0][0]["Not Specified"], 0)


class ValidateDocumentsDatasetTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test_documents()
        self.dataset_test_erratic = dataset_test_erratic()
        self.dataset_test_erratic_columns = dataset_test_erratic_columns()


    def test_validate_documents_dataset(self):
        validate = validate_documents_dataset(self.dataset_test)
        self.assertEqual(len(validate), 4)
        self.assertEqual(validate[0], "Some document last edition dates are longer than 10 characters. Count: 4")
        self.assertEqual(validate[2], "Some product identifiers length is not equal to  40 characters. Count: 4")
        self.assertEqual(validate[3], "Some document identifiers length is not equal to  40 characters. Count: 4")

    def test_validate_documents_dataset_erratic(self):
        validate = validate_documents_dataset(self.dataset_test_erratic)
        self.assertEqual(len(validate), 1)
        self.assertEqual(validate[0], "Dataset should have 15 columns")

    def test_validate_documents_dataset_erratic_columns(self):
        validate = validate_documents_dataset(self.dataset_test_erratic_columns)
        self.assertEqual(len(validate), 1)
        self.assertEqual(validate[0], "Dataset should have 15 columns")


class DocumentsDatasetCheckTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test_documents()


    def test_documents_dataset_check(self):
        check = documents_dataset_check(self.dataset_test)
        self.assertEqual(len(check),  2)
        self.assertEqual(check[0][0]["name"], "Document Title")
        self.assertEqual(check[0][0]["Longest String"], "TEST44")
        self.assertEqual(check[0][0]["Shortest String"], "T")
        self.assertEqual(check[0][0]["Not Specified"], 0)


class ValidateTopicsDatasetTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test_topics()
        self.dataset_test_erratic = dataset_test_erratic()
        self.dataset_test_erratic_columns = dataset_test_erratic_columns()


    def test_validate_topics_dataset(self):
        validate = validate_topics_dataset(self.dataset_test)
        self.assertEqual(len(validate), 2)
        self.assertEqual(validate[0], "Some document links don't contain 'reader'. Count: 4")
        self.assertEqual(validate[1], "Some document identifiers length is not equal to  40 characters. Count: 4")

    def test_validate_topics_dataset_erratic(self):
        validate = validate_topics_dataset(self.dataset_test_erratic)
        self.assertEqual(len(validate), 1)
        self.assertEqual(validate[0], "Dataset should have 6 columns")

    def test_validate_topics_dataset_erratic_columns(self):
        validate = validate_topics_dataset(self.dataset_test_erratic_columns)
        self.assertEqual(len(validate), 1)
        self.assertEqual(validate[0], "Dataset should have 6 columns")


class TopicsDatasetCheckTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test_topics()


    def test_topics_dataset_check(self):
        check = topics_dataset_check(self.dataset_test)
        self.assertEqual(len(check),  2)
        self.assertEqual(check[0][0]["name"], "Topic Title")
        self.assertEqual(check[0][0]["Longest String"], "TEST44")
        self.assertEqual(check[0][0]["Shortest String"], "T")
        self.assertEqual(check[0][0]["Not Specified"], 0)









