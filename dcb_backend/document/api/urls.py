from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.DocumentUpload.as_view(), name='upload'),
    path('remove', views.RemoveDocument.as_view(), name='remove'),
    path('list', views.ListDocuments.as_view(), name='list'),
    path('detail/<str:id>', views.DocumentDetail.as_view(), name='detail')
]