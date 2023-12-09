from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
import django.utils.http
import os
import uuid
from DCB_Backend import config
from document.models import DocumentModel
from .serializers import ListSerializer, RemoveSerializer, UploadSerializer
from .utils import Helper
from DCB_Backend import settings
from rest_framework.permissions import IsAuthenticated


class DocumentUpload(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadSerializer()
    parser_classes = (MultiPartParser,)

    @extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {"files": {"type": "string", "format": "binary"}},
            }
        },
    )
    def post(self, request):
        serializer = UploadSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None
            files = serializer.validated_data["files"]
            for file in files:
                realfilename, ext = os.path.splitext(file.name)
                random_uuid = str(uuid.uuid4())
                file.name = random_uuid + ext
                filepath = settings.UPLOADPATH + "/" + file.name
                model = DocumentModel.objects.create(
                    file=file,
                    uploaded_by=user,
                    name=realfilename,
                    vector_document_name=random_uuid,
                )
                Helper.add_pdf_to_vectorstore(config.VECTORSTORE, filepath, model.id)

            return Response(status=204)
        else:
            return Response(serializer.errors, status=400)


class RemoveDocument(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RemoveSerializer

    def post(self, request):
        document_id = request.data.get("id")
        document_model = DocumentModel.objects.get(id=document_id)

        Helper.delete_document(config.VECTORSTORE, document_model.id)

        document_model.delete()

        return Response(status=204)


class ListDocuments(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer
    queryset = DocumentModel.objects.all()


class DocumentDetail(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        methods=["GET"],
        responses={
            "multipart/form-data": {
                "type": "object",
                "properties": {"file": {"type": "string", "format": "binary"}},
            }
        },
    )
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        document = DocumentModel.objects.get(id=id)
        filecontent = document.file.file
        name = document.name

        response = HttpResponse(filecontent, content_type='application/pdf') #make dynamic later
        response["Content-Disposition"] = django.utils.http.content_disposition_header(
            False, name
        )

        return response
