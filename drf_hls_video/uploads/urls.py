from django.urls import path
from .views import UploadView, UploadDetailView

urlpatterns = [
    path('', UploadView.as_view()),
    path('<uuid:id>/', UploadDetailView.as_view()),
]
