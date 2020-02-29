from django.shortcuts import redirect, render

from db_manager.utils import database_upload


def db_upload(request):
    """Uncomment if refreshing data needed"""
    database_upload()
    return redirect('/')


def db_manager(request):
    return render(request, 'db-manager.html')
