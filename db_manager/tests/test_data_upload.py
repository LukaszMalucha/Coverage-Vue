import os

import pandas as pd
from django.conf import settings
from django.test import TestCase

from db_manager.data_upload import dataset_products_upload, dataset_documents_upload, dataset_topics_upload


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



