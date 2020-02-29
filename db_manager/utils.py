import csv
import json
import os.path
import re

import pandas as pd
from django.conf import settings

from core.models import DocumentModel

# FILE PATHS

documents_cleaned_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/documents_cleaned.csv")


def product_upload():
    """Upload products to database"""
    pass





def database_upload():
    """Upload scraped data to db"""
    # DELETE OLDER DATA FOR TEST
    documents = DocumentModel.objects.all()
    documents.delete()

    if documents_cleaned_path:
        with open(documents_cleaned_path, encoding="utf-8-sig") as f:
            reader = csv.reader(f)  # skip header
            next(reader, None)
            for row in reader:
                try:
                    _, created = DocumentModel.objects.get_or_create(
                        topic_title=row[0],
                        document_title=row[1],
                        document_number=row[2],
                        document_version=row[3],
                        document_revision=row[4],
                        document_type=row[5],
                        document_lang=row[6],
                        document_created_at=row[7],
                        document_last_edition=row[8],
                        document_last_publication=row[9],
                        document_revised_modified=row[10],
                        document_link=row[11],

                        product_name=row[12],
                        product_brand=row[13],
                        product_category=row[14],
                        product_code=row[15],
                        product_series=row[16],
                        product_part_number=row[17],

                        business=row[18],
                        maps_link=row[19],

                        # meta_category_bas=row[20],
                        # meta_category_ductedsystems=row[21],
                        # meta_category_visonic=row[22],
                        # meta_dita_id=row[23],
                        # meta_dita_mapPath=row[24],
                        # meta_baseId=row[25],
                        # meta_mapsId=row[26],
                        # meta_originId=row[27],
                    )
                except Exception as e:
                    pass
    else:
        pass
