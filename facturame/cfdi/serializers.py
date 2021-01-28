from rest_framework import serializers

from .models import CfdiModel

class CfdiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CfdiModel
        ordering = ['date_issued']
        fields = ('id', 'issuer_name', 'date_issued', 'issuer_rfc', 'cfdi_xml', 'total_ammount')