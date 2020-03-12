from django.shortcuts import redirect, render
from db_manager.utils import dataset_products_upload, dataset_documents_upload, dataset_topics_upload
import os
from django.conf import settings

import pandas as pd

dataset_test_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/dataset_test.csv")


def products_upload(request):
    """Upload products dataset"""
    dataset_products_upload()
    return redirect('/')


def documents_upload(request):
    """Upload products dataset"""
    dataset_documents_upload()
    return redirect('/')


def topics_upload(request):
    """Upload products dataset"""
    dataset_topics_upload()
    return redirect('/')


def db_manager(request):
    if request.method == 'POST':
        csv_file = request.FILES["csv_file"]
        data = pd.read_csv(csv_file, encoding='utf-8-sig')
        # DUPLCATY

        return render(request, 'db-manager.html', {'data': data.to_html()})

    return render(request, 'db-manager.html', {'data': "Empty"})
