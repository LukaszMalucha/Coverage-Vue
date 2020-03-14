from django.shortcuts import redirect, render
from db_manager.utils import dataset_products_upload, dataset_documents_upload, dataset_topics_upload
import os
from django.conf import settings
from django.urls import reverse
from db_manager.data_validation import dataset_check
import pandas as pd


# ADMIN PRIVILAGES
def products_upload(request):
    """Upload products dataset"""
    dataset_products_upload_bulk()
    return redirect("/")


def documents_upload(request):
    """Upload products dataset"""
    dataset_documents_upload()
    return redirect("/")


def topics_upload(request):
    """Upload products dataset"""
    dataset_topics_upload()
    return redirect("/")


def db_manager(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        # DUPLICATES
        head = data.head(20)
        meta, dataset_errors = dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_products_upload(data)
            except:
                report = ["Dataset upload wasn't successful due to error"]

            upload_report = report
            return render(request, "db-manager.html",
                          {"head": head.to_html(), "meta": meta, "upload_report": upload_report, "errors": dataset_errors})
        else:
            return render(request, "db-manager.html", {"head": head.to_html(), "meta": meta, "errors": dataset_errors})

    return render(request, "db-manager.html")
