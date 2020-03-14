import csv
import json
import os.path
import re

import pandas as pd
from django.conf import settings
from django.shortcuts import get_object_or_404
from core.models import DocumentModel, ProductModel, TopicModel
from datetime import datetime

# FILE PATHS

# documents_cleaned_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/documents_cleaned.csv")
dataset_products_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_products.csv")
dataset_documents_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_documents.csv")
dataset_topics_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_topics.csv")

# JOHNSON CONTROLS BRANDS

BRANDS = {'YORK', 'Johnson Controls', 'Metasys', 'Simplex', 'PENN Controls', 'Kantech',
          'Facility Explorer', 'LUX', 'CEM Systems', 'Exacq', 'Sensormatic', 'Tyco',
          'BCPro', 'Quantech', 'PEAK', 'Verasys', 'Ruskin', 'Not Specified', 'Autocall',
          'ShopperTrak', 'Triatek', 'ANSUL', 'PYRO-CHEM', 'WILLIAMS', 'CHEMGUARD',
          'Champion', 'Coleman', 'Fraser-Johnston', 'Luxaire', 'TempMaster', 'TrueVUE',
          'SKUM', 'HYGOOD', 'LPG', 'GEM', 'FIREATER', 'SABO FOAM', 'NEURUPPIN',
          'THORN SECURITY', 'Zettler'}


def dataset_products_upload(dataset):
    """Upload products to database """
    # DELETE OLDER DATA FOR TEST
    # products = ProductModel.objects.all()
    # products.delete()
    errors = []
    count_successful = 0
    count_duplicates = 0
    count_errors = 0
    for product in dataset.itertuples():
        duplicate = get_object_or_404(ProductModel, product_identifier=product.product_identifier)
        if duplicate:
            error_msg = f"{product.product_name} already in database"
            errors.append(error_msg)
            count_duplicates += 1
        else:
            try:
                product = ProductModel.objects.create(product_name=product.product_name,
                                                      product_brand=product.brand,
                                                      product_category=product.product_category,
                                                      product_code=product.product_code,
                                                      product_series=product.product_series,
                                                      business=product.business,
                                                      product_identifier=product.product_identifier
                                                      )

                count_successful += 1
            except Exception as e:
                error_msg = f"{product.product_name} was not uploaded due to error"
                errors.append(error_msg)
                count_errors += 1

    report = {"upload_errors": errors, "success": count_successful, "duplicate": count_duplicates, "errors": count_errors}

    return report


def dataset_documents_upload():
    """Upload documents to database"""
    # DELETE OLDER DATA FOR TEST
    documents = DocumentModel.objects.all()
    documents.delete()

    if dataset_documents_path:
        with open(dataset_documents_path, encoding="utf-8-sig") as f:
            reader = csv.reader(f)  # skip header
            next(reader, None)
            for row in reader:
                # try:
                related_product = get_object_or_404(ProductModel, product_identifier=row[13])
                date_created_at = datetime.strptime(row[6], "%Y-%m-%d")
                date_last_edition = datetime.strptime(row[7], "%Y-%m-%d")
                date_last_publication = datetime.strptime(row[8], "%Y-%m-%d")
                date_revised_modified = datetime.strptime(row[9], "%Y-%m-%d")

                _, created = DocumentModel.objects.get_or_create(
                    document_title=row[0],
                    document_number=row[1],
                    document_part_number=row[2],
                    document_version=row[3],
                    document_revision=row[4],
                    document_type=row[5],
                    document_created_at=date_created_at,
                    document_last_edition=date_last_edition,
                    document_last_publication=date_last_publication,
                    document_revised_modified=date_revised_modified,
                    document_brand=row[10],
                    document_link=row[11],
                    maps_link=row[12],
                    product=related_product,
                    document_identifier=row[14]
                )
                # except Exception as e:
                #     pass
    else:
        pass


def dataset_topics_upload():
    """Upload documents to database"""
    # DELETE OLDER DATA FOR TEST
    topics = TopicModel.objects.all()
    topics.delete()

    if dataset_topics_path:
        with open(dataset_topics_path, encoding="utf-8-sig") as f:
            reader = csv.reader(f)  # skip header
            next(reader, None)
            for row in reader:
                # try:
                related_document = get_object_or_404(DocumentModel, document_identifier=row[5])
                date_last_edition = datetime.strptime(row[3], "%Y-%m-%d")

                _, created = TopicModel.objects.get_or_create(
                    topic_title=row[0],
                    topic_breadcrumb=row[1],
                    topic_depth=row[2],
                    topic_last_edition=date_last_edition,
                    topic_link=row[4],
                    document=related_document
                )
                # except Exception as e:
                #     pass
    else:
        pass


def get_longest_string(dataset, column):
    values_list = list(dataset[column].unique())
    longest = max(values_list, key=len)
    return longest


def get_shortest_string(dataset, column):
    values_list = list(dataset[column].unique())
    shortest = min(values_list, key=len)
    return shortest


def get_na_count(dataset, column):
    na_count = len(dataset[dataset[column] == 'Not Specified'])
    return na_count


def get_missing_brands(dataset, column):
    column_brands = set(list(dataset[column].unique()))
    difference = column_brands - BRANDS
    difference = ', '.join(difference)
    return difference


def describe_column(dataset, column):
    column_dict = {}
    col_name = column.replace("_", " ")
    col_name = col_name.title()
    column_dict['name'] = col_name
    column_dict['Longest String'] = get_longest_string(dataset, column)
    column_dict['Shortest String'] = get_shortest_string(dataset, column)
    column_dict['Not Specified'] = get_na_count(dataset, column)

    return column_dict


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
        long_product_brand_count_count = long_product_brand.shape[0]
        if long_product_brand_count_count > 0:
            error_long_product_brand = f"Some brands are longer than 254 characters. Count: {long_product_brand_count_count}"
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


def dataset_products_upload_bulk():
    """Upload products to database 6:06"""
    # DELETE OLDER DATA FOR TEST
    products = ProductModel.objects.all()
    products.delete()

    if dataset_products_path:
        errors = []
        with open(dataset_products_path, encoding="utf-8-sig") as f:
            reader = csv.reader(f)  # skip header
            next(reader, None)
            for row in reader:
                try:
                    _, created = ProductModel.objects.get_or_create(
                        product_name=row[0],
                        product_brand=row[1],
                        product_category=row[2],
                        product_code=row[3],
                        product_series=row[4],
                        business=row[5],
                        product_identifier=row[6]
                    )
                except Exception as e:
                    pass
    else:
        pass
