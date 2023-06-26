from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
import csv

from .models import Lender
from .serializers import LenderSerializer


class LenderViewSet(viewsets.ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if request.accepted_renderer.format == "csv":
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="lenders.csv"'

            writer = csv.writer(response)
            writer.writerow(["id", "name", "email", "phone"])

            for lender in queryset:
                writer.writerow([lender.id, lender.name, lender.email, lender.phone])

            return response

        return Response(serializer.data)

    def create(self, request):
        if request.content_type == "text/csv":
            csvReader = csv.DictReader(request.data.decode("utf-8").splitlines())
            for row in csvReader:
                serializer = self.get_serializer(data=row)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)

        return super().create(request)
