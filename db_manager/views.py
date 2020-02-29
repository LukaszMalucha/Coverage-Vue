from django.shortcuts import redirect, render

from db_manager.utils import database_upload, dataset_products_upload, dataset_documents_upload, dataset_topics_upload


def db_upload(request):
    """Uncomment if refreshing data needed"""
    database_upload()
    return redirect('/')


def products_upload(request):
    """Upload products dataset"""
    dataset_product_upload()
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
    return render(request, 'db-manager.html')
