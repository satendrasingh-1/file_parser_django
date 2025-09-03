import threading
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .tasks import process_file   


class FileUploadView(APIView):
    def post(self, request, format=None):
        uploaded_file = request.FILES.get("file")
        if not uploaded_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        file_obj = UploadedFile.objects.create(
            filename=uploaded_file.name,
            file=uploaded_file,
            status="uploading",
            progress=0
        )

      
        threading.Thread(target=process_file, args=(file_obj,)).start()

        return Response(UploadedFileSerializer(file_obj).data, status=status.HTTP_201_CREATED)


class FileProgressView(APIView):
    def get(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        return Response({
            "file_id": str(file_obj.id),
            "status": file_obj.status,
            "progress": file_obj.progress
        })


class FileContentView(APIView):
    def get(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        if file_obj.status == "ready":
            return Response(file_obj.parsed_content)
        return Response({"message": "File upload or processing in progress. Please try again later."})


class FileListView(APIView):
    def get(self, request):
        files = UploadedFile.objects.all()
        return Response(UploadedFileSerializer(files, many=True).data)


class FileDeleteView(APIView):
    def delete(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        file_obj.delete()
        return Response({"message": "File deleted"}, status=status.HTTP_200_OK)


