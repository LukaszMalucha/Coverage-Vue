from django.shortcuts import redirect, render
from db_manager.data_upload import bulk_dataset_documents_upload, bulk_dataset_products_upload, bulk_dataset_topics_upload, dataset_documents_upload, dataset_topics_upload


import os
from django.conf import settings
from django.urls import reverse
from db_manager.data_validation import products_dataset_check, documents_dataset_check, topics_dataset_check
import pandas as pd


def db_manager(request):
    return render(request, "db-manager.html")


def products_upload(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        head = data.head(20)
        meta, dataset_errors = products_dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_products_upload(data)
            except:
                report = ["Dataset upload wasn't successful due to error"]

            upload_report = report
            return render(request, "products.html",
                          {"head": head.to_html(), "meta": meta, "upload_report": upload_report })
        else:
            return render(request, "products.html", {"head": head.to_html(), "meta": meta, "dataset_errors": dataset_errors})

    return render(request, "products.html")


def documents_upload(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        head = data.head(20)
        meta, dataset_errors = documents_dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_documents_upload(data)
            except:
                report = ["Dataset upload wasn't successful due to error"]

            upload_report = report
            return render(request, "documents.html",
                          {"head": head.to_html(), "meta": meta, "upload_report": upload_report})
        else:
            return render(request, "documents.html",
                          {"head": head.to_html(), "meta": meta, "dataset_errors": dataset_errors})

    return render(request, "documents.html")

def topics_upload(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        head = data.head(20)
        meta, dataset_errors = topics_dataset_check(data)
        if len(dataset_errors) == 0:
            try:
                report = dataset_topics_upload(data)
            except:
                report = ["Dataset upload wasn't successful due to error"]

            upload_report = report
            return render(request, "topics.html",
                          {"head": head.to_html(), "meta": meta, "upload_report": upload_report})
        else:
            return render(request, "topics.html",
                          {"head": head.to_html(), "meta": meta, "dataset_errors": dataset_errors})

    return render(request, "topics.html")


# ADMIN PRIVILEGES
def bulk_products_upload(request):
    """Upload products dataset"""
    bulk_dataset_products_upload()
    return redirect("/")


def bulk_documents_upload(request):
    """Upload products dataset"""
    bulk_dataset_documents_upload()
    return redirect("/")


def bulk_topics_upload(request):
    """Upload products dataset"""
    dataset_topics_upload()
    return redirect("/")