from rest_framework.serializers import FileField
from rest_framework import serializers
from document.models import DocumentModel


class UploadSerializer(serializers.Serializer):
    files = serializers.ListField(allow_empty=False ,child = FileField(max_length=1000, allow_empty_file=False, use_url=False
        )
    )

    def validate(self, data):
        allowed_file_types = ["application/pdf","text/plain"] # when editing list also add functionality to view
        files = data["files"]
        for file in files:
            if file.content_type not in allowed_file_types:
                raise serializers.ValidationError("FileType not allowed")
        return data


    class Meta:
        fields = ["files"]

class RemoveSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    class Meta:
        model = DocumentModel
        fields = ["id"]

class ListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    class Meta:
        model = DocumentModel
        fields = ["id","name"]
