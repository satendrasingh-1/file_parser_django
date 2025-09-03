from django.urls import path
from .views import FileUploadView, FileListView, FileDeleteView, FileProgressView, FileContentView

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file-upload"),
    path("", FileListView.as_view(), name="file-list"),
    path("<uuid:file_id>/delete/", FileDeleteView.as_view(), name="file-delete"),
    path("<uuid:file_id>/progress/", FileProgressView.as_view(), name="file-progress"),
    path("<uuid:file_id>/content/", FileContentView.as_view(), name="file-content"),
]
