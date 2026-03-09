from django.urls import path
from .views import UploadFileView , DownloadFileView

urlpatterns = [
    path("upload/", UploadFileView.as_view()),
    path("download/", DownloadFileView.as_view()),
]