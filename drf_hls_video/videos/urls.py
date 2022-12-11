from django.urls import path
from .views import HlsVideoList, HlsVideoDetail

urlpatterns = [
    path('', HlsVideoList.as_view()),
    path('<uuid:id>/', HlsVideoDetail.as_view()),
]
