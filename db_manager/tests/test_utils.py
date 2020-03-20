import os

import pandas as pd
from django.conf import settings
from django.test import TestCase

from db_manager.utils import get_longest_string, get_shortest_string, get_missing_brands, get_na_count, describe_column

dataset_test_path = os.path.join(settings.BASE_DIR, "db_manager/tests/dataset_test.csv")


def dataset_test():
    dataset = pd.read_csv(dataset_test_path, encoding="utf-8-sig")

    return dataset


def dataset_test_erratic():
    dataset = pd.read_csv(dataset_test_path, encoding="utf-8-sig")
    dataset.loc[len(dataset)] = [1, 2, 3, 4, 5, 6, 7]

    return dataset


class GetLongestStringTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()
        self.dataset_test_erratic = dataset_test_erratic()

    def test_get_longest_string(self):
        longest_string = get_longest_string(self.dataset_test, "product_name")
        self.assertEqual(longest_string, "TEST44")

    def test_get_longest_string_na(self):
        longest_string = get_longest_string(self.dataset_test_erratic, "product_name")
        self.assertEqual(longest_string, "N/A")


class GetShortestStringTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()
        self.dataset_test_erratic = dataset_test_erratic()

    def test_get_shortest_string(self):
        shortest_string = get_shortest_string(self.dataset_test, "product_name")
        self.assertEqual(shortest_string, "T")

    def test_get_shortest_string_na(self):
        shortest_string = get_shortest_string(self.dataset_test_erratic, "product_name")
        self.assertEqual(shortest_string, "N/A")


class GetNaCountTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()

    def test_get_na_count(self):
        na = get_na_count(self.dataset_test, "product_identifier")
        self.assertEqual(na, 1)


class GetMissingBrandsTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()

    def test_get_missing_brands(self):
        missing_brands = get_missing_brands(self.dataset_test, "brand")
        self.assertEqual(len(missing_brands), 109)


class DescribeColumnTest(TestCase):

    def setUp(self):
        self.dataset_test = dataset_test()

    def test_describe_column(self):
        col_dict = describe_column(self.dataset_test, "brand")
        self.assertEqual(col_dict, {'Longest String': 'TEST33', 'Not Specified': 0,
                                    'Shortest String': 'TEST1', 'name': 'Brand'})
