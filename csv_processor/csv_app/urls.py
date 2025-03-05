from django.urls import path
from .views import upload_csv, results

urlpatterns = [
    path("", upload_csv, name="upload_csv"),
    path("results/", results, name="results"),
]
