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

dataset_products_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_products.csv")
dataset_documents_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_documents.csv")
dataset_topics_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_topics.csv")


def dataset_products_upload(dataset):
    """Upload products to database """
    errors = []
    count_successful = 0
    count_duplicates = 0
    count_errors = 0
    for product in dataset.itertuples():
        if ProductModel.objects.filter(product_identifier=product.product_identifier).exists():
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
                error_msg = f"'{product.product_name}' was not uploaded due to error"
                errors.append(error_msg)
                count_errors += 1
                pass

    report = {"upload_errors": errors, "success": count_successful, "duplicate": count_duplicates,
              "errors": count_errors}

    return report


def dataset_documents_upload(dataset):
    """Upload products to database """
    errors = []
    count_successful = 0
    count_duplicates = 0
    count_errors = 0
    for document in dataset.itertuples():
        if DocumentModel.objects.filter(document_identifier=document.document_identifier).exists():
            error_msg = f"{document.document_title} already in database"
            errors.append(error_msg)
            count_duplicates += 1
        else:
            try:
                related_product = get_object_or_404(ProductModel, product_identifier=document.product_identifier)
                date_created_at = datetime.strptime(document.document_created_at, "%Y-%m-%d")
                date_last_edition = datetime.strptime(document.document_last_edition, "%Y-%m-%d")
                date_last_publication = datetime.strptime(document.document_last_publication, "%Y-%m-%d")
                date_revised_modified = datetime.strptime(document.document_revised_modified, "%Y-%m-%d")

                document = DocumentModel.objects.create(
                    document_title=document.document_title,
                    document_number=document.document_number,
                    document_part_number=document.document_part_number,
                    document_version=document.document_version,
                    document_revision=document.document_revision,
                    document_type=document.document_type,
                    document_created_at=date_created_at,
                    document_last_edition=date_last_edition,
                    document_last_publication=date_last_publication,
                    document_revised_modified=date_revised_modified,
                    document_brand=document.brand,
                    document_link=document.document_link,
                    maps_link=document.maps_link,
                    product=related_product,
                    document_identifier=document.document_identifier
                )
                count_successful += 1
            except Exception as e:
                error_msg = f"'{document.document_title}' was not uploaded due to error"
                errors.append(error_msg)
                count_errors += 1
                pass

    report = {"upload_errors": errors, "success": count_successful, "duplicate": count_duplicates,
              "errors": count_errors}

    return report


def dataset_topics_upload(dataset):
    """Upload products to database """
    errors = []
    count_successful = 0
    count_updates = 0
    count_errors = 0
    for topic in dataset.itertuples():
        if TopicModel.objects.filter(topic_breadcrumb=topic.breadcrumb).exists():
            TopicModel.objects.filter(topic_breadcrumb=topic.breadcrumb).delete()
            error_msg = f"Previous version of '{topic.topic_title}' deleted from the database"
            errors.append(error_msg)
            count_updates += 1
        else:
            try:
                related_document = get_object_or_404(DocumentModel, document_identifier=topic.document_identifier)
                date_last_edition = datetime.strptime(topic.document_last_edition, "%Y-%m-%d")
                topic = TopicModel.objects.create(
                    topic_title=topic.topic_title,
                    topic_breadcrumb=topic.breadcrumb,
                    topic_depth=topic.topic_depth,
                    topic_last_edition=date_last_edition,
                    topic_link=topic.document_link,
                    document=related_document
                )
                count_successful += 1
            except Exception as e:
                error_msg = f"'{topic.topic_title}' was not uploaded due to error"
                errors.append(error_msg)
                count_errors += 1
                pass
    report = {"upload_errors": errors, "success": count_successful, "updates": count_updates,
              "errors": count_errors}

    return report


def bulk_products_upload():
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


def bulk_documents_upload():
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


def bulk_topics_upload():
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
