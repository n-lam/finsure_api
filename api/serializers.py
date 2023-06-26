from rest_framework import serializers
from .models import Lender


class FileSerializer(serializers.Serializer):
    # TODO: Add a max length
    file = serializers.CharField()


class LenderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def validate_code(self, value: str):
        if len(value) != 3:
            serializers.ValidationError("Invalid code: 3 characters are required.")
        elif not value.isalpha():
            serializers.ValidationError("Invalid code: Only letters are allowed.")
        normalisedValue = value.upper()
        return normalisedValue

    class Meta:
        model = Lender
        fields = "__all__"
