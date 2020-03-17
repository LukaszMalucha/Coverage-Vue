import os
import pandas as pd

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django_pandas.io import read_frame

from core.models import DocumentModel

from db_manager.data_validation import products_dataset_check, documents_dataset_check, topics_dataset_check
from db_manager.data_upload import dataset_products_upload, dataset_documents_upload, dataset_topics_upload
from db_manager.data_upload import bulk_documents_upload, bulk_products_upload, bulk_topics_upload


def db_manager(request):
    return render(request, "db-manager.html")


def products_upload(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "products.html",
                          {"critical_error": critical_error, })

        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        meta, dataset_errors = products_dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_products_upload(data)
            except:
                critical_error = "Dataset upload wasn't successful due to error"
                return render(request, "products.html",
                              {"critical_error": critical_error, })

            upload_report = report
            return render(request, "products.html",
                          {"meta": meta, "upload_report": upload_report, })

        else:
            return render(request, "products.html",
                          {"meta": meta, "dataset_errors": dataset_errors})

    return render(request, "products.html")


def documents_upload(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "products.html",
                          {"critical_error": critical_error, })
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        meta, dataset_errors = documents_dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_documents_upload(data)
            except:
                critical_error = "Dataset upload wasn't successful due to error"
                return render(request, "products.html",
                              {"critical_error": critical_error, })

            upload_report = report
            return render(request, "documents.html",
                          {"meta": meta, "upload_report": upload_report})
        else:
            return render(request, "documents.html",
                          {"meta": meta, "dataset_errors": dataset_errors})

    return render(request, "documents.html")


def topics_upload(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "products.html",
                          {"critical_error": critical_error, })
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        meta, dataset_errors = topics_dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_topics_upload(data)
            except:
                critical_error = "Dataset upload wasn't successful due to error"
                return render(request, "products.html",
                              {"critical_error": critical_error, })

            upload_report = report
            return render(request, "topics.html",
                          {"meta": meta, "upload_report": upload_report})

        else:
            return render(request, "topics.html",
                          {"meta": meta, "dataset_errors": dataset_errors})



    return render(request, "topics.html")




def download_queryset(request):
    qs = DocumentModel.objects.filter(document_brand="Autocall")
    q = "Autocall"
    df = read_frame(qs)
    csv = df.to_csv(encoding='utf-8-sig', index=False)
    response = HttpResponse(csv, content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={q}.csv'

    return response



# ADMIN PRIVILEGES
def bulk_products(request):
    """Upload products dataset"""
    bulk_products_upload()
    return redirect("/")


def bulk_documents(request):
    """Upload products dataset"""
    bulk_documents_upload()
    return redirect("/")


def bulk_topics(request):
    """Upload products dataset"""
    bulk_topics_upload()
    return redirect("/")
