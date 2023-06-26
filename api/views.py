from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets, status
from rest_framework.response import Response
import csv

from .models import Lender
from .serializers import FileSerializer, LenderSerializer


class LenderViewSet(viewsets.ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer

    def list(self, request: HttpRequest):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if request.GET.get("filetype") == "csv":
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="lenders.csv"'

            writer = csv.writer(response)
            writer.writerow(["name", "code", "upfront_commission_rate", "trial_commission_rate", "active"])

            for lender in queryset:
                writer.writerow(
                    [
                        lender.name,
                        lender.code,
                        lender.upfront_commission_rate,
                        lender.trial_commission_rate,
                        lender.active,
                    ]
                )

            return response

        return Response(serializer.data)

    def create(self, request: HttpRequest):
        # For some reason, DRF doesn't seem to like uploading raw CSV files, so
        # I have to send the CSV file wrapped inside a JSON payload.
        if request.query_params.get("filetype") == "csv":
            serializer = FileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            file = request.data["file"]
            csvReader = csv.DictReader(file.splitlines())
            createdRows = []
            for row in csvReader:
                serializer = self.get_serializer(data=row)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                createdRows.append(row)

            headers = self.get_success_headers(serializer.data)
            return Response(createdRows, status=status.HTTP_201_CREATED, headers=headers)

        return super().create(request)
