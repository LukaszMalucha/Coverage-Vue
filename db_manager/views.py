import pandas as pd
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from db_manager.data_upload import bulk_documents_upload, bulk_products_upload, bulk_topics_upload
from db_manager.data_upload import dataset_products_upload, dataset_documents_upload, dataset_topics_upload
from db_manager.data_validation import products_dataset_check, documents_dataset_check, topics_dataset_check
from core.models import ProductModel, DocumentModel, TopicModel
from datetime import datetime

@user_passes_test(lambda u: u.is_superuser)
def db_manager(request):
    return render(request, "db-manager.html")



@user_passes_test(lambda u: u.is_superuser)
def products_upload(request):
    """Product dataset upload to database"""
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "products.html",
                          {"critical_error": critical_error, })

        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        meta, dataset_errors = products_dataset_check(data)
        meta_1 = meta[:6]
        meta_2 = meta[6:]
        if len(dataset_errors) == 0:
            try:
                report = dataset_products_upload(data)
            except:
                critical_error = "Dataset upload wasn't successful due to error"
                return render(request, "products.html",
                              {"critical_error": critical_error, })

            upload_report = report
            return render(request, "products.html",
                          {"meta_1": meta_1, "meta_2": meta_2, "upload_report": upload_report, })

        else:
            return render(request, "products.html",
                          {"meta_1": meta_1, "meta_2": meta_2, "dataset_errors": dataset_errors})

    return render(request, "products.html")

@user_passes_test(lambda u: u.is_superuser)
def documents_upload(request):
    """Document dataset upload to database"""
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "products.html",
                          {"critical_error": critical_error, })
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        meta, dataset_errors = documents_dataset_check(data)
        meta_1 = meta[:6]
        meta_2 = meta[6:]
        if len(dataset_errors) == 0:
            try:
                report = dataset_documents_upload(data)
            except:
                critical_error = "Dataset upload wasn't successful due to error"
                return render(request, "products.html",
                              {"critical_error": critical_error, })

            upload_report = report
            return render(request, "documents.html",
                          {"meta_1": meta_1, "meta_2": meta_2, "upload_report": upload_report, })
        else:
            return render(request, "documents.html",
                          {"meta_1": meta_1, "meta_2": meta_2, "dataset_errors": dataset_errors})

    return render(request, "documents.html")

@user_passes_test(lambda u: u.is_superuser)
def topics_upload(request):
    """Topics dataset upload to database"""
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "products.html",
                          {"critical_error": critical_error, })
        data = pd.read_csv(csv_file, encoding="utf-8-sig")
        meta, dataset_errors = topics_dataset_check(data)
        meta_1 = meta[:6]
        meta_2 = meta[6:]
        if len(dataset_errors) == 0:
            try:
                report = dataset_topics_upload(data)
            except:
                critical_error = "Dataset upload wasn't successful due to error"
                return render(request, "products.html",
                              {"critical_error": critical_error, })

            upload_report = report
            return render(request, "topics.html",
                          {"meta_1": meta_1, "meta_2": meta_2, "upload_report": upload_report, })

        else:
            return render(request, "topics.html",
                          {"meta_1": meta_1, "meta_2": meta_2, "dataset_errors": dataset_errors})

    return render(request, "topics.html")


@user_passes_test(lambda u: u.is_superuser)
def bulk_products(request):
    """Upload products dataset"""
    bulk_products_upload()
    return redirect("/")

@user_passes_test(lambda u: u.is_superuser)
def bulk_documents(request):
    """Upload documents dataset"""
    bulk_documents_upload()
    return redirect("/")

@user_passes_test(lambda u: u.is_superuser)
def bulk_topics(request):
    """Upload topics dataset"""
    bulk_topics_upload()
    return redirect("/")

@user_passes_test(lambda u: u.is_superuser)
def bulk_delete(request):
    """Delete today's uploads"""
    ProductModel.objects.filter(uploaded=datetime.today().strftime('%Y-%m-%d')).delete()
    DocumentModel.objects.filter(uploaded=datetime.today().strftime('%Y-%m-%d')).delete()
    TopicModel.objects.filter(uploaded=datetime.today().strftime('%Y-%m-%d')).delete()
    return redirect("/")
