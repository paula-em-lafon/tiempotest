import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CfdiModel

from .serializers import CfdiSerializer

class PaginationTestCase(APITestCase):
    def setUp(self):
        self.Cfdi1 = CfdiModel.objects.create(issuer_name="jose",\
            issuer_rfc="RFCRFCRFCRFCR",\
             cfdi_xml="<some>xml</some>",\
             total_ammount=85.43)
        self.Cfdi2 = CfdiModel.objects.create(issuer_name="agustín",\
            issuer_rfc="RFCRFCRFCRFCR",\
             cfdi_xml="<some>xml</some>",\
             total_ammount=85.43)
        self.Cfdi2 = CfdiModel.objects.create(issuer_name="sonia",\
            issuer_rfc="RFCRFCRFCRFCR",\
             cfdi_xml="<some>xml</some>",\
             total_ammount=42.43)

    def test_pagination(self):
        response = self.client.get("/cfdilist/?page=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['issuer_name'], "jose")
        self.assertEqual(response.data['results'][0]['issuer_rfc'], 'RFCRFCRFCRFCR')
        self.assertEqual(response.data['results'][0]['cfdi_xml'], '<some>xml</some>')
        self.assertEqual(response.data['results'][0]['total_ammount'], '85.43')

class PaginationErrorCase(APITestCase):
    def setUp(self):
        self.Cfdi1 = CfdiModel.objects.create(issuer_name="jose",\
            issuer_rfc="RFCRFCRFCRFCR",\
             cfdi_xml="<some>xml</some>",\
             total_ammount=85.43)
        self.Cfdi2 = CfdiModel.objects.create(issuer_name="agustín",\
            issuer_rfc="RFCRFCRFCRFCR",\
             cfdi_xml="<some>xml</some>",\
             total_ammount=85.43)
        self.Cfdi2 = CfdiModel.objects.create(issuer_name="sonia",\
            issuer_rfc="RFCRFCRFCRFCR",\
             cfdi_xml="<some>xml</some>",\
             total_ammount=42.43)

    def test_pagination(self):
        response = self.client.get("/cfdilist/?page=3")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)