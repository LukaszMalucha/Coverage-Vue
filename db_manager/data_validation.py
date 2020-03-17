from django.shortcuts import redirect, render
import os
from django.conf import settings
from db_manager.utils import get_longest_string, get_shortest_string, get_na_count, get_missing_brands, describe_column

import pandas as pd


def validate_products_dataset(dataset):
    errors = []

    required_columns = {'product_name', 'brand', 'product_category', 'product_code', 'product_series', 'business',
                        'product_identifier'}
    dataset_columns = set(dataset.columns.values)
    if len(dataset_columns) != 7:
        error_column = f"Dataset should have 7 columns"
        errors.append(error_column)
        return errors

    col_difference = dataset_columns - required_columns
    col_difference = ', '.join(col_difference)
    if len(col_difference) > 0:
        error_column = f"Invalid columns in dataset: {col_difference}"
        errors.append(error_column)
        return errors

    if len(col_difference) == 0:
        long_product_names = dataset[dataset['product_name'].str.len() > 254]
        long_product_names_count = long_product_names.shape[0]
        if long_product_names_count > 0:
            error_long_product_names = f"Some product names are longer than 254 characters. Count: {long_product_names_count}"
            errors.append(error_long_product_names)

        long_product_brand = dataset[dataset['brand'].str.len() > 254]
        long_product_brand_count = long_product_brand.shape[0]
        if long_product_brand_count > 0:
            error_long_product_brand = f"Some brands are longer than 254 characters. Count: {long_product_brand_count}"
            errors.append(error_long_product_brand)

        long_product_category = dataset[dataset['product_category'].str.len() > 254]
        long_product_category_count = long_product_category.shape[0]
        if long_product_category_count > 0:
            error_long_product_category = f"Some product categories are longer than 254 characters. Count: {long_product_category_count}"
            errors.append(error_long_product_category)

        long_product_series = dataset[dataset['product_series'].str.len() > 254]
        long_product_series_count = long_product_series.shape[0]
        if long_product_series_count > 0:
            error_long_product_series = f"Some product series are longer than 254 characters. Count: {long_product_series_count}"
            errors.append(error_long_product_series)

        long_business = dataset[dataset['business'].str.len() > 254]
        long_business_count = long_business.shape[0]
        if long_business_count > 0:
            error_long_business = f"Some product businesses are longer than 254 characters. Count: {long_business_count}"
            errors.append(error_long_business)

        invalid_brands = get_missing_brands(dataset, 'brand')
        if len(invalid_brands) > 0:
            error_invalid_brands = f"Invalid brands in dataset: {invalid_brands}"
            errors.append(error_invalid_brands)

        product_id_erratic = dataset[dataset['product_identifier'].str.len() != 40]
        product_id_erratic_count = product_id_erratic.shape[0]
        if product_id_erratic_count > 0:
            error_product_id_erratic = f"Some product identifiers length is not equal to  40 characters. Count: {product_id_erratic_count}"
            errors.append(error_product_id_erratic)

        check_na = dataset.isnull().values.any()
        if check_na:
            error_check_na = f"NaN present in dataset"
            errors.append(error_check_na)

    return errors


def products_dataset_check(dataset):
    columns = list(dataset.columns)

    columns_metadata = []
    for column in columns:
        dict_col = describe_column(dataset, column)
        if column == "brand":
            dict_col['New Brands:'] = get_missing_brands(dataset, column)
        columns_metadata.append(dict_col)

    validation_errors = validate_products_dataset(dataset)

    return columns_metadata, validation_errors


def validate_documents_dataset(dataset):
    errors = []

    required_columns = {'document_title', 'document_number', 'document_part_number', 'document_version',
                        'document_revision', 'document_type', 'document_created_at', 'document_last_edition',
                        'document_last_publication', 'document_revised_modified', 'brand', 'document_link', 'maps_link',
                        'product_identifier', 'document_identifier'}

    dataset_columns = set(dataset.columns.values)
    if len(dataset_columns) != 15:
        error_column = f"Dataset should have 15 columns"
        errors.append(error_column)
        return errors

    col_difference = dataset_columns - required_columns
    col_difference = ', '.join(col_difference)
    if len(col_difference) > 0:
        error_column = f"Invalid columns in dataset: {col_difference}"
        errors.append(error_column)
        return errors

    if len(col_difference) == 0:
        long_document_titles = dataset[dataset['document_title'].str.len() > 254]
        long_document_titles_count = long_document_titles.shape[0]
        if long_document_titles_count > 0:
            error_long_document_titles = f"Some titles are longer than 254 characters. Count: {long_document_titles_count}"
            errors.append(error_long_document_titles)

        long_document_number = dataset[dataset['document_number'].str.len() > 254]
        long_document_number_count = long_document_number.shape[0]
        if long_document_number_count > 0:
            error_long_document_number = f"Some document numbers are longer than 254 characters. Count: {long_document_number_count}"
            errors.append(error_long_document_number)

        long_document_part_number = dataset[dataset['document_part_number'].str.len() > 254]
        long_document_part_number_count = long_document_part_number.shape[0]
        if long_document_part_number_count > 0:
            error_long_document_part_number = f"Some document part numbers are longer than 254 characters. Count: {long_document_part_number_count}"
            errors.append(error_long_document_part_number)

        long_document_version = dataset[dataset['document_version'].str.len() > 254]
        long_document_version_count = long_document_version.shape[0]
        if long_document_version_count > 0:
            error_long_document_version = f"Some document versions are longer than 254 characters. Count: {long_document_version_count}"
            errors.append(error_long_document_version)

        long_document_revision = dataset[dataset['document_revision'].str.len() > 254]
        long_document_revision_count = long_document_revision.shape[0]
        if long_document_revision_count > 0:
            error_long_document_revision = f"Some document revisions are longer than 254 characters. Count: {long_document_revision_count}"
            errors.append(error_long_document_revision)

        long_document_type = dataset[dataset['document_type'].str.len() > 254]
        long_document_type_count = long_document_type.shape[0]
        if long_document_type_count > 0:
            error_long_document_type = f"Some document numbers are longer than 254 characters. Count: {long_document_type_count}"
            errors.append(error_long_document_type)

        long_document_created_at = dataset[dataset['document_created_at'].str.len() != 10]
        long_document_created_at_count = long_document_created_at.shape[0]
        if long_document_created_at_count > 0:
            error_long_document_created_at = f"Some document creation dates are longer than 10 characters. Count: {long_document_created_at_count}"
            errors.append(error_long_document_created_at)

        long_document_last_edition = dataset[dataset['document_last_edition'].str.len() != 10]
        long_document_last_edition_count = long_document_last_edition.shape[0]
        if long_document_last_edition_count > 0:
            error_long_document_last_edition = f"Some document last edition dates are longer than 10 characters. Count: {long_document_last_edition_count}"
            errors.append(error_long_document_last_edition)

        long_document_last_publication = dataset[dataset['document_last_publication'].str.len() != 10]
        long_document_last_publication_count = long_document_last_publication.shape[0]
        if long_document_last_publication_count > 0:
            error_long_document_last_publication = f"Some document last publication dates are longer than 10 characters. Count: {long_document_last_publication_count}"
            errors.append(error_long_document_last_publication)

        long_document_revised_modified = dataset[dataset['document_revised_modified'].str.len() != 10]
        long_document_revised_modified_count = long_document_revised_modified.shape[0]
        if long_document_revised_modified_count > 0:
            error_long_document_revised_modified = f"Some document last revision dates are longer than 10 characters. Count: {long_document_revised_modified_count}"
            errors.append(error_long_document_revised_modified)

        invalid_brands = get_missing_brands(dataset, 'brand')
        if len(invalid_brands) > 0:
            error_invalid_brands = f"Invalid brands in dataset: {invalid_brands}"
            errors.append(error_invalid_brands)

        product_id_erratic = dataset[dataset['product_identifier'].str.len() != 40]
        product_id_erratic_count = product_id_erratic.shape[0]
        if product_id_erratic_count > 0:
            error_product_id_erratic = f"Some product identifiers length is not equal to  40 characters. Count: {product_id_erratic_count}"
            errors.append(error_product_id_erratic)

        document_id_erratic = dataset[dataset['document_identifier'].str.len() != 40]
        document_id_erratic_count = document_id_erratic.shape[0]
        if document_id_erratic_count > 0:
            error_document_id_erratic = f"Some document identifiers length is not equal to  40 characters. Count: {document_id_erratic_count}"
            errors.append(error_document_id_erratic)

        check_na = dataset.isnull().values.any()
        if check_na:
            error_check_na = f"NaN present in dataset"
            errors.append(error_check_na)

    return errors


def documents_dataset_check(dataset):
    columns = list(dataset.columns)

    columns_metadata = []
    for column in columns:
        dict_col = describe_column(dataset, column)
        if column == "brand":
            dict_col['New Brands:'] = get_missing_brands(dataset, column)
        columns_metadata.append(dict_col)

    validation_errors = validate_documents_dataset(dataset)

    return columns_metadata, validation_errors


def validate_topics_dataset(dataset):
    errors = []

    required_columns = {'topic_title', 'breadcrumb', 'topic_depth', 'document_last_edition', 'document_link',
                        'document_identifier'}
    dataset_columns = set(dataset.columns.values)
    if len(dataset_columns) != 6:
        error_column = f"Dataset should have 6 columns"
        errors.append(error_column)
        return errors

    col_difference = dataset_columns - required_columns
    col_difference = ', '.join(col_difference)
    if len(col_difference) > 0:
        error_column = f"Invalid columns in dataset: {col_difference}"
        errors.append(error_column)
        return errors

    if len(col_difference) == 0:
        long_topic_titles = dataset[dataset['topic_title'].str.len() > 254]
        long_topic_titles_count = long_topic_titles.shape[0]
        if long_topic_titles_count > 0:
            error_long_topic_titles = f"Some titles are longer than 254 characters. Count: {long_topic_titles_count}"
            errors.append(error_long_topic_titles)

        invalid_document_link = dataset[~dataset['document_link'].str.contains("reader")]
        invalid_document_link_count = invalid_document_link.shape[0]
        if invalid_document_link_count > 0:
            error_invalid_document_link = f"Some document links don't contain 'reader'. Count: {invalid_document_link_count}"
            errors.append(error_invalid_document_link)

        long_document_last_edition = dataset[dataset['document_last_edition'].str.len() != 10]
        long_document_last_edition_count = long_document_last_edition.shape[0]
        if long_document_last_edition_count > 0:
            error_long_document_last_edition = f"Some document last edition dates are longer than 10 characters. Count: {long_document_last_edition_count}"
            errors.append(error_long_document_last_edition)

        document_id_erratic = dataset[dataset['document_identifier'].str.len() != 40]
        document_id_erratic_count = document_id_erratic.shape[0]
        if document_id_erratic_count > 0:
            error_document_id_erratic = f"Some document identifiers length is not equal to  40 characters. Count: {document_id_erratic_count}"
            errors.append(error_document_id_erratic)

        check_na = dataset.isnull().values.any()
        if check_na:
            error_check_na = f"NaN present in dataset"
            errors.append(error_check_na)

    return errors


def topics_dataset_check(dataset):
    columns = list(dataset.columns)

    columns_metadata = []
    for column in columns:
        dict_col = describe_column(dataset, column)
        columns_metadata.append(dict_col)

    validation_errors = validate_topics_dataset(dataset)

    return columns_metadata, validation_errors
