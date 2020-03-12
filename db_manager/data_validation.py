from django.shortcuts import redirect, render
from db_manager.utils import dataset_products_upload, dataset_documents_upload, dataset_topics_upload
import os
from django.conf import settings
from db_manager.utils import get_longest_string, get_shortest_string, get_na_count, get_missing_brands, validate_column

import pandas as pd


def validate_products_dataset(dataset):

    columns = list(dataset.columns)

    columns_metadata = []
    for column in columns:
        dict_col = validate_column(dataset, column)
        if column == "brand":
            dict_col['New Brands:'] = get_missing_brands(dataset, column)
        columns_metadata.append(dict_col)


    return columns_metadata





