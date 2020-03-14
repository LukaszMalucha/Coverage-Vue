from django.shortcuts import redirect, render
from db_manager.utils import dataset_products_upload, dataset_documents_upload, dataset_topics_upload
import os
from django.conf import settings
from db_manager.utils import get_longest_string, get_shortest_string, get_na_count, get_missing_brands, describe_column, validate_products_dataset

import pandas as pd



def dataset_check(dataset):
    columns = list(dataset.columns)

    columns_metadata = []
    for column in columns:
        dict_col = describe_column(dataset, column)
        if column == "brand":
            dict_col['New Brands:'] = get_missing_brands(dataset, column)
        columns_metadata.append(dict_col)

    validation_errors = validate_products_dataset(dataset)

    return columns_metadata, validation_errors




