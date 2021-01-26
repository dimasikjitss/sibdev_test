from django.urls import path
from .views import CvsLoadView, ProcessedFileView
urlpatterns = [
    path('csv_load/', CvsLoadView.as_view()),
    path('proccesed_file/', ProcessedFileView.as_view()),
]
