from django.shortcuts import redirect, render

from db_manager.utils import dataset_products_upload, dataset_documents_upload


def products_upload(request):
    """Upload products dataset"""
    dataset_products_upload()
    return redirect('/')


def documents_upload(request):
    """Upload products dataset"""
    dataset_documents_upload()
    return redirect('/')


def db_manager(request):
    return render(request, 'db-manager.html')
