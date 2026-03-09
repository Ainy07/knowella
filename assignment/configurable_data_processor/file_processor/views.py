import os
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import process_file, save_to_db
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from django.conf import settings


class UploadFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        file = request.FILES.get("file")

        if not file:
            return Response({"error": "File not provided"}, status=400)

        file = request.FILES.get("file")

        if not file:
            return Response({"error": "File not provided"}, status=400)

        if file.name.endswith(".csv"):
            df = pd.read_csv(file)

        elif file.name.endswith(".xlsx"):
            df = pd.read_excel(file)

        else:
            return Response({"error": "Unsupported file format"}, status=400)

        os.makedirs("uploads", exist_ok=True)

        upload_path = "uploads/temp.csv"

        df.to_csv(upload_path, index=False)

        processed_df = process_file(upload_path)

        save_to_db(processed_df)

        processed_df.to_csv("uploads/output.csv", index=False)

        return Response({
            "message": "File processed successfully"
        })
        
        
        


class DownloadFileView(APIView):

    def get(self, request):

        file_path = "uploads/output.csv"

        if not os.path.exists(file_path):
            return Response({"error": "File not found"}, status=404)

        return FileResponse(open(file_path, "rb"), as_attachment=True, filename="output.csv")        